using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace game
{
    public class Mob
    {
        public int maxHP;
        public int maxMana;

        public int currentHP;
        public int currentMana;

        public int HPregen;
        public int manaRegen;

        public string Name { get; set; }

        public Dictionary<string, double> valnurabilities;

        public Mob()
        {
            Console.WriteLine("Called constructor from Mob");
        }

        public void DealDamage(Mob target, Damage damage)
        {

        }
        public static void initialiseMob(Mob mob)
        {
            Console.WriteLine("initialiseMob called with {0}", mob.Name);
            mob.currentMana = mob.maxMana;
            mob.currentHP = mob.maxHP;
        }
    }
}
