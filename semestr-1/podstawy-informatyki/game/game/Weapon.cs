﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace game
{
    public class Weapon : Item
    {
        public Damage damage;

        public Weapon(Damage damage)
        {
            this.damage = damage;
        }
    }
}
