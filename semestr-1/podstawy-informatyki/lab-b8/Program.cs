using System;
using System.Collections.Generic;

namespace B8
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<HighestPeak> peaksOfEurope = Homework.CreateList();

            // A
            Console.WriteLine("A):");
            foreach (HighestPeak peak in peaksOfEurope)
            {
                if(peak.Country == "Austria") {
                    peak.ShowInfo();
                }
            }

            // B
            Console.WriteLine("\nB):");
            peaksOfEurope[peaksOfEurope.Count - 2].ShowInfo();

            // C
            Console.WriteLine("\nC):");
            int heightSum = 0;
            foreach(HighestPeak peak in peaksOfEurope)
            {
                heightSum += peak.Elevation;
            }
            Console.WriteLine("Średnia arytmetyczna: {0}", heightSum / peaksOfEurope.Count);

            // D
            Console.WriteLine("\nD):");
            foreach (HighestPeak peak in peaksOfEurope)
            {
                if(peak.Elevation >= 4000 && peak.Elevation <= 5000) {
                    peak.ShowInfo();
                }
            }
            // E
            Console.WriteLine("\nE):");
            peaksOfEurope.Sort((x,y) => x.Elevation.CompareTo(y.Elevation));
            for(int i = 0; i < 10; i++) {
                peaksOfEurope[i].ShowInfo();
            }
        }
    }
}
