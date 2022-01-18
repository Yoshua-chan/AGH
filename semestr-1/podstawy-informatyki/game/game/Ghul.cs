using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace game
{
    public class Ghul : Monster
    {
        public static Random rnd = new Random();
        public Damage mainAttack = new Damage();
        public Damage poisonAttack = new Damage();
        public Ghul()
        {
            this.Name = "Ghul";
            
            this.maxHP = 150;
            this.maxMana = 50;

            this.valnurabilities["silver"] = 1.5;
            this.valnurabilities["fire"] = 1.6;

            this.mainAttack.damage["slash"] = 30;

            this.poisonAttack.damage["poison"] = 15;
            this.poisonAttack.damage["poisoned"] = 3;

            Mob.initialiseMob(this);
        }

        public override void Attack(Player target)
        {
            if (target.hasYrden)
            {
                this.currentHP -= Convert.ToInt32(target.yrdenDamage * this.valnurabilities["magic"]);
                target.hasYrden = false;
                return;
            }
            else 
            {
                if(rnd.NextDouble() < 0.9)
                {
                    this.DealDamage(target, mainAttack);;
                }
                else
                {
                    this.DealDamage(target, poisonAttack);
                }


            }
            

        }
        ~Ghul()
        {
            Console.WriteLine("Destructor called for Ghul");
        }
    }
}
