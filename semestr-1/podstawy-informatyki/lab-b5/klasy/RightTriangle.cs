using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace klasy
{
    class RightTriangle
    {
        // pola klasy przechowujace dlugosci przyprostokatnych
        private double a;
        private double b;
        private string name;

        enum color
        {
            Red,
            Green,
            Blue
        }
        // wlasciwosci klasy odpowiadajace powyzszym polom
        public double A
        {
            get { return a; } // prosty getter - tylko zwraca wartosc
            set // setter - pozwoli ustawic wartosc tylko jesli jest dodatnia
            {
                if (value > 0) a = value; // prosze zwrocic uwage na slowo kluczowe value
            }
        }
        public double B
        {
            get { return b; } // prosty getter - tylko zwraca wartosc
            set // setter - pozwoli ustawic wartosc tylko jesli jest dodatnia
            {
                if (value > 0) b = value;
            }
        }
        // metoda klasy obliczajaca tangens kata w trojkacie A/B
        // zwyczajowa kolejnosc podawania elementow klasy: pola, własciwosci, metody
        public double ComputeTangent()
        {
            return A / B;
        }
        private double ComputeC()
        {
            return Math.Sqrt(a * a + b * b);
        }
        public double ComputeSine()
        {
            return a / this.ComputeC();
        }
        public double Circumference
        {
            get { return a + b + this.ComputeC(); }
            private set {}
        }

        public string Name
        {
            get { return name; }
            set { name = value; }
        }
        
    }
}
