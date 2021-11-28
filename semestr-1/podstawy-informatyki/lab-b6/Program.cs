using System;

namespace lab_b6
{
    class Program
    {
        static void Main(string[] args)
        {
            MarathonRace run1 = new MarathonRace("Yoshua", "Chan", 2137);
            Console.WriteLine("Forename: {0}, Lastname: {1}, Run time: {2}", run1.Forename, run1.Lastname, run1.RunTime);

            MarathonRace copy = new MarathonRace(run1);
            Console.WriteLine("Forename: {0}, Lastname: {1}, Run time: {2}", copy.Forename, copy.Lastname, copy.RunTime);
        }
    }
}
