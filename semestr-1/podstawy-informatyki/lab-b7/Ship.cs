using System;


namespace lab_b7
{
    public class Ship
    {
        //TODO: obiekt klasy Engine reprezentujący silnik (możliwy do odczytania i ustawiania) 
        //      ● prywatna zmienna int przechowująca masę niezaładowanego statku (bez produktów) 
        //      ● konstruktor domyślny proponujący jakieś wartości dla powyższych zmiennych 
        //      ● konstruktor parametryczny pozwalający ustawić powyższe zmienne (masa statku musi być dodatnia) 
        //TODO: ● publiczna  metoda  bool  TravelOffer(Destination,  Product,  Product),  która  wczyta  ofertę 
        //TODO: podróży  do  wybranego  portu  docelowego  (pierwszy  argument)  wraz  z  przewozem  dwóch 
        //TODO: wybranych  produktów  (drugi  i  trzeci  argument).  Dla  uproszczenia  zakładamy,  że  statek 
        //TODO: zawsze  będzie  przewoził  dokładnie  dwa  obiekty  typu  Product.  Metoda  powinna  wykonać 
        //TODO: następujące czynności: 
        //      o obliczyć całkowitą cenę sprzedaży proponowanego ładunku 
        //TODO: o obliczyć  całkowity  koszt  podróży  do  proponowanego  portu,  korzystając  z  metody 
        //TODO: zawartej w dołączonej klasie Engine 
        //TODO: o zdecydować, czy oferta jest opłacalna – zakładamy, że podróż opłaci się tylko wtedy, 
        //TODO: gdy cena sprzedaży przewyższy koszty o co najmniej 1000 
        //TODO: o jeśli oferta jest opłacalna, wypisać na ekran czytelne informacje o akceptacji oferty, 
        //TODO: zawartości  i  masie  ładunku,  czasie  podróży  (pomocna  może  być  metoda  z  klasy 
        //TODO: Engine), całkowitej cenie sprzedaży i koszcie podróży 
        //TODO: o jeśli oferta jest nieopłacalna, wystarczy wyświetlić informację o odrzuceniu oferty 
        //TODO: o w obydwu wypadkach należy zwrócić bool informujący o akceptacji (lub nie) oferty 
        //TODO: ● opcjonalnie także inne, prywatne metody – jeśli uznają Państwo, że mogą być przydatne
        private int mass;
        public Engine Engine { get; set; }
        public Ship()
        {
            this.Engine = new Engine(Engine.Fuel.Hydrogen);
            this.mass = 100000;
        }
        public Ship(Engine ShipEngine, int Mass)
        {
            this.Engine = ShipEngine;
            if (Mass > 0)
                this.mass = Mass;
            else
                this.mass = 0;
        }
        private void PrintDetails(Destination destination, Product p1, Product p2, int TravelTime, int p1Price, int p2Price)
        {
            Console.WriteLine("Trade offer accepted!");
            Console.WriteLine("Offer details:");
            Console.WriteLine("\tTravel time: {0}", TravelTime);
            Console.WriteLine("\tProduct 1:");
			Console.WriteLine("\t\tName: {0}", p1.Name);
			Console.WriteLine("\t\tMass: {0}", p1.Name);
			Console.WriteLine("\t\tCurrent market price: {0}", p1Price);
            Console.WriteLine("\tProduct 2:");
			Console.WriteLine("\t\tName: {0}", p2.Name);
			Console.WriteLine("\t\tMass: {0}", p2.Name);
			Console.WriteLine("\t\tCurrent market price: {0}", p2Price);
        }
        public bool TravelOffer(Destination destination, Product product1, Product product2)
        {
            int p1Price = product1.CurrentPrice;
            int p2Price = product1.CurrentPrice;
            int cargoPrice = p1Price * product1.Mass
                           + p2Price * product2.Mass;

            int travelCost = Engine.TravelCost(destination.distance, this.mass + product1.Mass + product2.Mass);

            if (cargoPrice > travelCost + 1000)
            {
                PrintDetails(destination, product1, product2, 
                Engine.TravelTime(destination.distance, this.mass + product1.Mass + product2.Mass), 
                p1Price, p2Price);

                return true;
            }
            else
            {
                Console.WriteLine("Trade offer rejected :c");
                return false;
            }

        }
    }
}
