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
            this.items = new List<Item>();

            Damage steelSwordDamage = new Damage();
            steelSwordDamage.damage.Add("steel", 51);

            Damage silverSwordDamage = new Damage();
            silverSwordDamage.damage.Add("silver", 40); //40 before

            this.firstSword = new Weapon(steelSwordDamage, "Steel sword");
            this.secondSword = new Weapon(silverSwordDamage, "Silver sword");
        }
        public void Add(string name)
        {
            items.Add(new Item(name));
        }

        public void PickUp(Item item)
        {

        }
        public void Use(int index)
        {

        }
    }
}
