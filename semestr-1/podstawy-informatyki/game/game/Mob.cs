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

        public int stunned;
        public int onFire;
        public int poisoned;
        public int poisonDamage;

        public string Name { get; set; }

        public Dictionary<string, double> valnurabilities;

        public Mob()
        {
            //Console.WriteLine("Called constructor from {0} ", this.Name);
            this.valnurabilities = new Dictionary<string, double>();

            this.poisoned = 0; // gets updated at the end of turn, takes damage at the beginning
            this.stunned = 0; // gets updated at the end of turn, skips turn if non zeros
            this.onFire = 0; // gets updated at the end of turn, takes damage at the 
            this.valnurabilities["silver"] = 1.0;
            this.valnurabilities["fire"] = 1.0;
            this.valnurabilities["steel"] = 1.0;
            this.valnurabilities["frost"] = 1.0;
            this.valnurabilities["magic"] = 1.0;
            this.valnurabilities["poison"] = 1.0;
            this.valnurabilities["slash"] = 1.0;
        }

        ~Mob()
        {
            Console.WriteLine("Called destructor from {0} ", this.Name);
        }

        public static bool IsDead(Mob mob)
        {
            return (mob.currentHP <= 0) ? true : false;
        }

        public void DealDamage(Mob target, Damage damage)
        {
            try
            {
                foreach (KeyValuePair<string, double> kvp in damage.damage)
                {
                    if (kvp.Key == "stun")
                    {
                        target.stunned += Convert.ToInt32(kvp.Value);
                        continue;
                    }
                    else if (kvp.Key == "poisoned")
                    {
                        target.poisoned += Convert.ToInt32(kvp.Value);
                        continue;

                    } else if(kvp.Key == "poison")
                    {
                        target.poisonDamage = Convert.ToInt32(kvp.Value);
                    }
                    try
                    {
                        target.currentHP -= Convert.ToInt32(kvp.Value * target.valnurabilities[kvp.Key]);
                        Console.WriteLine("Damage dealt to {0} of {1} - {2}", target.Name, kvp.Value * target.valnurabilities[kvp.Key], kvp.Key);
                        Console.WriteLine("Current healt of {0}: {1} HP", target.Name, target.currentHP);
                    }
                    catch (KeyNotFoundException ex)
                    {
                        continue;
                    }

                }
            }
            catch(NullReferenceException ex)
            {
                return;
            }
        }
        public static void initialiseMob(Mob mob)
        {
            Console.WriteLine("initialiseMob called with {0}", mob.Name);
            mob.currentMana = mob.maxMana;
            mob.currentHP = mob.maxHP;
        }
    }
}
