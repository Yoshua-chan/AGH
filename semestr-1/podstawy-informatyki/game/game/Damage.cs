using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace game
{
    public class Damage
    {
        public Dictionary<string, double> damage;

        public Damage()
        {
            this.damage = new Dictionary<string, double>();
        }
        public Damage(Damage damage) // copying constructor
        {
            Damage newDamage = new Damage();
            foreach (KeyValuePair<string, double> kvp in damage.damage) {
                this.damage.Add(kvp.Key, kvp.Value);
            }
        }
    }
}
