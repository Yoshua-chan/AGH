using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace game
{
    public class Player : Mob
    {
        public Inventory inventory = new Inventory();
        public Player()
        {
            Console.WriteLine("Called constructor from Player");
            this.Name = "Gerwazy";
            this.maxHP = 300;
            this.maxMana = 100;
    



            Mob.initialiseMob(this);

        }
    }
}
