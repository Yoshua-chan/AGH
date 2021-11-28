using System;

namespace Chess
{
    class Program
    {
        static void Main(string[] args)
        {
            ChessPlayer player1 = new ChessPlayer("Bobby Crabber", 85, 64);
            ChessPlayer player2 = new ChessPlayer("Alexander Kalmarov", 78, 55);

            ChessMatch match = new ChessMatch(player1, player2);    

            match.printAll();

            Console.WriteLine("The winner is {0}", match.GetWinner());
            
        }
    }
}
