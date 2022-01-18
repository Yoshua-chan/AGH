using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace game
{
    public static class Combat
    {
        public static List<Monster> enemies = new List<Monster>();
        public static int enemyChoice = 0;
        public static void Draw()
        {
            Console.SetCursorPosition(0, 0);
            for(int i = 0; i < 25; i++)
            {
                for(int j = 0; j < 70; j++)
                {
                    if (j == 0 || j == 69 || i == 0 || i == 24)
                        Console.Write('█');
                    else
                        Console.Write(' ');
                }
                Console.Write('\n');
            }
            /*
            Console.SetCursorPosition(1, 1);
            for(int i = 0; i < 23; i++)
            {
                for (int j = 0; j < 48; j++)
                {
                    Console.Write(' ');
                }
                Console.SetCursorPosition(1, i + 1);
            } */
            for(int i = 0; i < enemies.Count; i++)
            {
                Console.SetCursorPosition(13 + i * 19, 5);
                Console.Write(enemies[i].Name);
                Console.SetCursorPosition(13 + i * 19 - 3, 7);
                Console.Write("HP: {0}/{1}", Convert.ToString(enemies[i].currentHP).PadLeft(3), enemies[i].maxHP);
                Console.SetCursorPosition(13 + i * 19 + 1, 9);
                Console.Write("[{0}]", enemyChoice == i ? 'x' : ' ');
            }
        }
        public static void SetEnemies(List<Monster> enemiesList)
        {
            enemies = enemiesList;
        }
        public static void PreviousEnemy()
        {
            if(enemyChoice > 0)
                enemyChoice--;
        }
        public static void NextEnemy()
        {
            if (enemyChoice < enemies.Count - 1)
                enemyChoice++;
        }
    }
}
