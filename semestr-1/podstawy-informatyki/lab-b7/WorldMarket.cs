using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab_b7
{
    class WorldMarket
    {
        private static Random rnd = new Random();
        public static int GetInitialPricePerKg()
        {
            return rnd.Next() % 900 + 100; 
        }
        public static int GetNewPricePerKg(int initial)
        {
            return initial + (rnd.Next() % 250 - 50);
        }
    }
}
