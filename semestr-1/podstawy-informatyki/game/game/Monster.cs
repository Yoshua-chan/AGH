using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace game
{
    public class Monster : Mob
    {
        public Dictionary<Tuple<string, int>, Damage> attacks;

        public Monster()
        {
            this.attacks = new Dictionary<Tuple<string, int>, Damage>();
        }
            
        public virtual void Attack(Player target)
        {
            if (target.hasYrden)
            {
                
                this.currentHP -= Convert.ToInt32(target.yrdenDamage * this.valnurabilities["magic"]);
                target.hasYrden = false;
                return;
            } else if (true)
            {

            }

        }
    }
}
