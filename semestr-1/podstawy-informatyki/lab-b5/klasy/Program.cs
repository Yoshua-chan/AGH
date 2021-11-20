using System;

namespace klasy
{
    class Program
    {
        static void Main(string[] args)
        {
            RightTriangle tr1 = new RightTriangle();
            RightTriangle tr2 = new RightTriangle();
            RightTriangle tr3 = new RightTriangle();

            tr1.A = 3;
            tr1.B = 4;
            Console.WriteLine("tr1 Circumference: {0}", tr1.Circumference);
            Console.WriteLine("tr1 Sine: {0}", tr1.ComputeSine());
            
            tr2.A = 6;
            tr2.B = 8;
            Console.WriteLine("tr2 Circumference: {0}", tr2.Circumference);
            Console.WriteLine("tr2 Sine: {0}", tr2.ComputeSine());

            tr3.A = 1;
            tr3.B = 1;
            Console.WriteLine("tr3 Circumference: {0}", tr3.Circumference);
            Console.WriteLine("tr3 Sine: {0}", tr3.ComputeSine());
        }
    }
}
