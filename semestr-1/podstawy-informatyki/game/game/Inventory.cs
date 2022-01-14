using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace game
{
    public class Inventory
    {
        public Weapon firstSword;
        public Weapon secondSword;

        public List<Item> items;

        public Inventory()
        {
            Damage steelSwordDamage = new Damage();
            steelSwordDamage.damage.Add("steel", 50);

            Damage silverSwordDamage = new Damage();
            silverSwordDamage.damage.Add("silver", 40);

            this.firstSword = new Weapon(silverSwordDamage);
        }
    }
}
