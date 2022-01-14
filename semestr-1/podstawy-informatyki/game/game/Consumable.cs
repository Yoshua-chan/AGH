using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace game
{
    public class Consumable : Item
    {

        public class Swallow : Consumable
        {

        }

        public class Oriole : Consumable // wilga
        {

        }

        public class Blizzard: Consumable
        {

        }

        public class TownyOwl: Consumable // puszczyk - zwieksza regeneracje many
        {

        }
    }
    //TODO: Wilga (neutralizuje debuffy), Jaskółka (regeneracja hp), Zamieć (daje ci dodatkową turę)
}
