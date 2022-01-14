using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace game
{
    public class Ghul : Monster
    {
        public Ghul()
        {
            this.maxHP = 300;
            this.maxMana = 50;

            this.valnurabilities.Add("silver", 1.5);
            this.valnurabilities.Add("fire", 1.6);

            Mob.initialiseMob(this);
        }
    }
}
