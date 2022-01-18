using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace game
{
    public static class BottomUI
    {
        public static int verticalOffset;
        public static int height;
        public static int width;
        private static int barSegments = 12;
        private static Player player;

        public static void SetPlayer(Player newPlayer)
        {
            player = newPlayer;
        }
        public static void Draw()
        {
            height = 10;
            //width = 50;

            Console.SetCursorPosition(0, verticalOffset);
            for (int i = 0; i < height; i++)
            {
                for (int j = 0; j < width; j++)
                {
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
                    {
                        Console.Write(' ');
                    }
                }
                Console.Write('\n');
            }
            // HP Bar
            Console.SetCursorPosition(6, verticalOffset + 2);
            Console.Write("HP");
            Console.SetCursorPosition(2, verticalOffset + 3);
            DrawHPBar(player);

            // Mana Bar
            Console.SetCursorPosition(6, verticalOffset + 5);
            Console.Write("Mana");
            Console.SetCursorPosition(2, verticalOffset + 6);
            DrawManaBar(player);


            int statsOffset = 25;

            //States
            if(player.stunned != 0)
            {
                Console.SetCursorPosition(statsOffset, verticalOffset + 2);
                Console.WriteLine("Stunned for: {0}", player.stunned);
            }
            if(player.hasYrden)
            {
                Console.SetCursorPosition(statsOffset, verticalOffset + 3);
                Console.WriteLine("Yrden damage: {0}", player.yrdenDamage);
            }
            if(player.onFire != 0)
            {
                Console.SetCursorPosition(statsOffset, verticalOffset + 4);
                Console.WriteLine("On fire for: {0}", player.onFire);
            }

            if(player.poisoned != 0)
            {
                Console.SetCursorPosition(statsOffset, verticalOffset + 5);
                Console.WriteLine("Poisoned for: {0}", player.poisoned);

                Console.SetCursorPosition(statsOffset, verticalOffset + 6);
                Console.WriteLine("Poisoned damage: {0}", player.poisonDamage);

            }
            if(player.orioleTime != 0)
            {
                Console.SetCursorPosition(statsOffset, verticalOffset + 7);
                Console.WriteLine("Oriole: {0}", player.orioleTime);
            }

            switch(player.currentAttackType)
            {
                case 0:
                    DrawAttacks(verticalOffset, 48);
                break;
                case 1:
                    DrawSwords(verticalOffset, 48);
                break;
                case 2:
                    DrawSigns(verticalOffset, 48);
                break;
                case 3:
                    DrawInventory(verticalOffset, 48);
                break;

            }

            Console.SetCursorPosition(0, 0);

        }

        private static void DrawHPBar(Player player)
        {
            int totalSegments = barSegments;
            int activeSegments = Convert.ToInt32(totalSegments * player.currentHP / player.maxHP);
            
            //int activeSegment = Convert.ToInt32(totalSegments * 0.5);
            Console.Write(Convert.ToString(player.currentHP).PadRight(4));
            for (int i = 0; i < activeSegments; i++)
            {
                Console.Write('█');
            }
            for (int i = 0; i < totalSegments - activeSegments; i++)
            {
                Console.Write('░');
            }
        }

        private static void DrawManaBar(Player player)
        {
            int totalSegments = barSegments;
            int activeSegments = Convert.ToInt32(totalSegments * player.currentMana / player.maxMana);
            //int activeSegment = Convert.ToInt32(totalSegments * 0.5);
            Console.Write(Convert.ToString(player.currentMana).PadRight(4));
            for (int i = 0; i < activeSegments; i++)
            {
                Console.Write('█');
            }
            for(int i = 0; i < totalSegments - activeSegments; i++)
            {
                Console.Write('░');
            }
        }

        public static void SetWidth(int new_width)
        {
            width = new_width;
        }
        public static void SetOffset(int offset)
        {
            verticalOffset = offset;
        }
        public static void DrawAttacks(int topOffset, int leftOffset)
        {
            // Available stuff


            //Sword attacc
            Console.SetCursorPosition(leftOffset, topOffset + 2);
            Console.Write("[{0}] Sword attack", player.choice == 1 ? 'x' : ' ');
            Console.SetCursorPosition(leftOffset, topOffset + 4);
            Console.Write("[{0}] Signs", player.choice == 2 ? 'x' : ' ');
            Console.SetCursorPosition(leftOffset, topOffset + 6);
            Console.Write("[{0}] Inventory", player.choice == 3 ? 'x' : ' ');
        }

        public static void DrawSigns(int topOffset, int leftOffset)
        {
            // Available stuff


            //Sword attacc
            Console.SetCursorPosition(leftOffset, topOffset + 2);
            Console.Write("[{0}] Back", player.choice == 1 ? 'x' : ' ');
            Console.SetCursorPosition(leftOffset, topOffset + 3);
            Console.Write("[{0}] Aard", player.choice == 2 ? 'x' : ' ');
            Console.SetCursorPosition(leftOffset, topOffset + 4);
            Console.Write("[{0}] Igni", player.choice == 3 ? 'x' : ' ');
            Console.SetCursorPosition(leftOffset, topOffset + 5);
            Console.Write("[{0}] Yrden", player.choice == 4 ? 'x' : ' ');
            Console.SetCursorPosition(leftOffset, topOffset + 6);
            Console.Write("[{0}] Quen", player.choice == 5 ? 'x' : ' ');
        }

        public static void DrawSwords(int topOffset, int leftOffset)
        {
            //Sword attacc
            Console.SetCursorPosition(leftOffset, topOffset + 2);
            Console.Write("[{0}] Back", player.choice == 1 ? 'x' : ' ');
            Console.SetCursorPosition(leftOffset, topOffset + 4);
            Console.Write("[{0}] Steel sword", player.choice == 2 ? 'x' : ' ');
            Console.SetCursorPosition(leftOffset, topOffset + 6);
            Console.Write("[{0}] Silver sword", player.choice == 3 ? 'x' : ' ');
        }
        public static void DrawInventory(int topOffset, int leftOffset)
        {
            int pos = 0;
            Console.SetCursorPosition(leftOffset, topOffset + 2);
            Console.Write("[{0}] Back", player.choice == pos + 1 ? 'x' : ' ');
            foreach(Item item in player.inventory.items)
            {                
                Console.SetCursorPosition(leftOffset, topOffset + 3 + pos);
                Console.Write("[{0}] {1}", player.choice == pos + 2 ? 'x' : ' ', player.inventory.items[pos].Name);
                pos++;
            }
        }
    }
}
