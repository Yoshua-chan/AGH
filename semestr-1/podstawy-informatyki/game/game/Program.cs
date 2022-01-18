using System;
using System.Collections.Generic;

namespace game
{
    public class Program
    {
        public enum GameState
        {
            map,
            combat,
            dialog
        }
        public enum Turns
        {
            player,
            enemy
        }
        public enum CombatState
        {
            selectEnemy,
            selectAction
        }
        public static bool turnEffectsApplies = false;
        public static Turns whoseTurn = Turns.player;
        public static CombatState combatState = CombatState.selectEnemy;
        public static GameState state = GameState.map;
        static void Main(string[] args)
        {


            Player gerwazy = new Player();
            gerwazy.choice = 0;
            gerwazy.position.room = 0;
            //gerwazy.currentHP = 1;

            

            /*List<Monster> enemies = new List<Monster>();
            enemies.Add(new Ghul());
            enemies.Add(new Ghul());
            enemies.Add(new Ghul()); */

            List<MonsterEntity> MonsterList = new List<MonsterEntity> { 
                new MonsterEntity(new Position(0, 15, 20)),
                new MonsterEntity(new Position(0, 4, 5))
            };

            List<Monster> temp1 = new List<Monster>();
            temp1.Add(new Ghul());
            temp1.Add(new Ghul());
            temp1.Add(new Ghul());
            MonsterList[0].content = temp1;

            List<Monster> temp2 = new List<Monster>();
            temp2.Add(new Ghul());
            temp2.Add(new Ghul());
            MonsterList[1].content = temp2;

            //Combat.SetEnemies(enemies);
            Map.Initialize();
            Map.SetPlayer(gerwazy);

            BottomUI.SetPlayer(gerwazy);
            BottomUI.SetWidth(70);
            BottomUI.SetOffset(26);

            Console.SetWindowSize(BottomUI.width, BottomUI.height + Map.height);
            Console.CursorVisible = false;

            state = GameState.map;
            combatState = CombatState.selectEnemy;

            Map.Draw(gerwazy.position.room, MonsterList);
            BottomUI.Draw();
           



            //gerwazy.currentHP = 100;

            while (true)
            {
                if (state == GameState.map) // Map loop
                {
                    combatState = CombatState.selectEnemy;
                    Move(gerwazy);
                    for(int i = 0; i < MonsterList.Count; i++)
                    {
                        MonsterList[i].Move();
                        if(MonsterList[i].CheckForPlayer(gerwazy) == true)
                        {
                            //throw new Exception();

                            Combat.SetEnemies(MonsterList[i].content);
                            MonsterList.RemoveAt(i);
                            state = GameState.combat;

                        }
                    }
                    if(gerwazy.position.x == 6 && gerwazy.position.y == 19)
                    {
                        Map.OpenDoor();
                        Map.mapArray[0, 19, 6] = 5;
                    }
                    if (gerwazy.position.x == 5 && gerwazy.position.y == 5 && Map.mapArray[0, 5, 5] == 2)
                    {
                        gerwazy.inventory.Add("Swallow");
                        gerwazy.inventory.Add("Tawny Owl");
                        Console.SetCursorPosition(0, 25);
                        Console.Write("Potions added to inventory.");
                        Map.mapArray[0, 5, 5] = 0;
                    }
                    if(Map.NearJaskier() == true)
                    {
                        state = GameState.dialog;
                        DisplayEnding();
                    }
                    Map.Draw(gerwazy.position.room, MonsterList);
                }
                else if (state == GameState.combat) // Combat loop
                {
                    if (whoseTurn == Turns.player) // Player's turn
                    {
                        if(gerwazy.currentHP <= 0)
                        {
                            GameOver();
                        }
                        if (turnEffectsApplies == false)
                        {
                            if (gerwazy.poisoned > 0)
                            {
                                gerwazy.currentHP -= Convert.ToInt32(gerwazy.poisonDamage * gerwazy.valnurabilities["poison"]);
                            }
                            if (gerwazy.orioleTime > 0)
                            {
                                gerwazy.orioleTime--;
                            }
                            if (gerwazy.orioleTime == 0)
                            {
                                gerwazy.valnurabilities["poison"] = 1.0;
                            }
                            turnEffectsApplies = true;
                        }
                        Move(gerwazy);
                        Combat.Draw();
                        
                    }
                    else if(whoseTurn == Turns.enemy)
                    {
                        Combat.enemies.RemoveAll(Mob.IsDead);
                        Combat.enemyChoice = 0;
                        if (Combat.enemies.Count == 0)
                        {
                            Console.WriteLine("Moby zdechły");
                            state = GameState.map;
                        }
                        else
                        {
                            try
                            {
                                foreach (Monster enemy in Combat.enemies)
                                {
                                    if (enemy.onFire > 0)
                                    {
                                        enemy.currentHP -= Convert.ToInt32(enemy.valnurabilities["fire"] * 40);
                                        enemy.onFire--;
                                    }
                                    enemy.Attack(gerwazy);
                                    System.Threading.Thread.Sleep(500);
                                }
                            }
                            catch(Exception ex)
                            {
                                whoseTurn = Turns.player;
                                state = GameState.map;
                            }
                        }
                        turnEffectsApplies = false;
                        whoseTurn = Turns.player;
                    }
                }
                BottomUI.Draw();
                Console.SetCursorPosition(0, 36);
                Console.WriteLine("gracz: x = {0}, y = {1}", gerwazy.position.x, gerwazy.position.y);
                //System.Threading.Thread.Sleep(250);

            }


        }
        public static void Move(Player player)
        {
            ConsoleKeyInfo input;
            input = Console.ReadKey();
            if (state == GameState.map)
            {
                if (input.Key == ConsoleKey.UpArrow)
                    player.MoveUp();
                else if (input.Key == ConsoleKey.DownArrow)
                    player.MoveDown();
                else if (input.Key == ConsoleKey.LeftArrow)
                    player.MoveLeft();
                else if (input.Key == ConsoleKey.RightArrow)
                    player.MoveRight();
            }
            else if (state == GameState.combat)
            {
                if (input.Key == ConsoleKey.LeftArrow)
                {
                    Combat.PreviousEnemy();
                }
                else if (input.Key == ConsoleKey.RightArrow)
                {
                    Combat.NextEnemy();
                }
                else
                {
                    //return 0;
                }

                if (input.Key == ConsoleKey.UpArrow)
                    player.PreviousChoice();
                else if (input.Key == ConsoleKey.DownArrow)
                    player.NextChoice();
                else if (input.Key == ConsoleKey.Spacebar || input.Key == ConsoleKey.Enter)
                {
                    int val = player.Select();
                    if (val == 1)
                    {
                        whoseTurn = Turns.enemy;
                    }
                    else if(val == 2)
                    {
                        player.DealDamage(Combat.enemies[Combat.enemyChoice], player.inventory.firstSword.damage);
                        whoseTurn = Turns.enemy;
                    }
                    else if(val == 3)
                    {
                        player.DealDamage(Combat.enemies[Combat.enemyChoice], player.inventory.secondSword.damage);
                        whoseTurn = Turns.enemy;
                    }
                    else if(val == 4)
                    {
                        player.Aard(Combat.enemies[Combat.enemyChoice]);
                        whoseTurn = Turns.enemy;
                    }
                    else if(val == 5)
                    {
                        player.Igni(Combat.enemies[Combat.enemyChoice]);
                        whoseTurn = Turns.enemy;
                    }
                }
                else
                {
                    //return 0;
                }

            }
        }
        public static void DisplayEnding()
        {

            int width = 50;
            int height = 12;
            for(int i = 0; i < height; i++)
            {
                for(int j = 0; j < width; j++)
                {
                    Console.SetCursorPosition(j + 10, i + 3);
                    if (i == 0 && j == 0)
                    {
                        Console.Write('╔');
                    }
                    else if (i == 0 && j == width - 1)
                    {
                        Console.Write('╗');
                    }
                    else if (i == height - 1 && j == 0)
                    {
                        Console.Write('╚');
                    }
                    else if (i == height - 1 && j == width - 1)
                    {
                        Console.Write('╝');
                    }
                    else if (i == height - 1 || i == 0)
                    {
                        Console.Write('═');
                    }
                    else if (j == 0 || j == width - 1)
                    {
                        Console.Write('║');
                    }
                    else
                        Console.Write(' ');
                }

                Console.SetCursorPosition(13, 5);
                Console.Write("Jaskier:");
                Console.SetCursorPosition(13, 7);
                Console.Write("Dzięki za ratunek, Geralt!");
                Console.SetCursorPosition(13, 9);
                Console.Write("Niestety, Ciri jest w innym lochu...");

            }
            while(true)
            {
                ConsoleKeyInfo input;
                input = Console.ReadKey();
                if(input.Key == ConsoleKey.Enter || input.Key == ConsoleKey.Spacebar)
                {
                    Console.SetCursorPosition(0, 36);
                    Environment.Exit(0);
                }
            }
        }
        public static void GameOver()
        {
            int width = 45;
            int height = 12;
            for (int i = 0; i < height; i++)
            {
                for (int j = 0; j < width; j++)
                {
                    Console.SetCursorPosition(j + 13, i + 3);
                    if (i == 0 && j == 0)
                    {
                        Console.Write('╔');
                    }
                    else if (i == 0 && j == width - 1)
                    {
                        Console.Write('╗');
                    }
                    else if (i == height - 1 && j == 0)
                    {
                        Console.Write('╚');
                    }
                    else if (i == height - 1 && j == width - 1)
                    {
                        Console.Write('╝');
                    }
                    else if (i == height - 1 || i == 0)
                    {
                        Console.Write('═');
                    }
                    else if (j == 0 || j == width - 1)
                    {
                        Console.Write('║');
                    }
                    else
                        Console.Write(' ');
                }
                Console.SetCursorPosition(30, 6);
                Console.Write("GAME OVER!");

                Console.SetCursorPosition(20, 8);
                Console.Write("Press Space or Enter to exit...");
            }
            while (true)
            {
                ConsoleKeyInfo input;
                input = Console.ReadKey();
                if (input.Key == ConsoleKey.Enter || input.Key == ConsoleKey.Spacebar)
                {
                    Console.SetCursorPosition(0, 36);
                    Environment.Exit(0);
                }
            }
        }
    }
}
