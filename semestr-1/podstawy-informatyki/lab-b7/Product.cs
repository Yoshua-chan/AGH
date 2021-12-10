using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab_b7
{
    public class Product
    {
        
        
        private int mass;
        private int currentPrice;
        public string Name { get; private set; }
        public int Mass
        {
            get
            {
                return this.mass;
            }
            set
            {
                if (value > 0)
                    this.mass = value;
            }
        }

        public int CurrentPrice {
            get {
                this.currentPrice = WorldMarket.GetNewPricePerKg(this.currentPrice);
                return this.currentPrice;
            }
        }

        public Product(string Name)
        {
            this.Name = Name;
            this.Mass = 0;  
            this.currentPrice = WorldMarket.GetInitialPricePerKg();
        }
        public Product(string Name, int Mass)
        {
            this.Name = Name;
            this.Mass = Mass;
            this.currentPrice = WorldMarket.GetInitialPricePerKg();
        }

        int GetCurrentValue()
        {
            return this.Mass * this.currentPrice;
        }

    }
}
