﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace game
{
    public class Item
    {
        public string Name { get; set; }
        public Item(string name)
        {
            this.Name = name;
        }
        public Item()
        {
            this.Name = "Item";
        }

    }
}
