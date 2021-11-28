using System;

namespace hello
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(SumDivisibleBy7(0, 0, 40));
        }

        static int Binsearch(int value, int[] arr, int left, int right) { // Zadanie G
            int middle;

            if(left <= right) {
                middle = (right + left) / 2;
                if(value < arr[middle])
                    return Binsearch(value, arr, left, middle - 1);
                else if (value > arr[middle])
                    return Binsearch(value, arr, middle + 1, right);
                else
                    return middle;
            }
            else return -1;
        }
        static double Solution(double a, double b, double c) // Zadanie H
        {
            double delta = b * b - 4 * a * c;
            if(delta < 0)
                return double.NaN;
            
            return (-b - Math.Sqrt(delta)) / (2 * a);
        }

        static int SumDivisibleBy7(int current_sum, int left, int right) { // Zadanie I
            if(left <= right) {
                if(left % 7 == 0)
                    return current_sum + left + SumDivisibleBy7(current_sum, left + 1, right);
                else
                    return current_sum + SumDivisibleBy7(current_sum, left + 1, right);
            } else
                return 0;
        }
    }

    
}
