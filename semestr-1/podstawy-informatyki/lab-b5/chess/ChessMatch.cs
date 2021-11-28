using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Chess
{
    class ChessMatch
    {
        public ChessPlayer player1;
        public ChessPlayer player2;

        public enum Levels
        {
            local,
            national,
            international
        }


        public ChessMatch(ChessPlayer player1, ChessPlayer player2)
        {
            this.player1 = player1;
            this.player2 = player2;
        }

        public string GetWinner()
        {
            if (player1.Skill > player2.Skill)
                return player1.Name;
            else
                return player2.Name;
        }
        public void printAll() {
            Console.WriteLine("Player 1:");
            Console.WriteLine("Name: {0}\nAge: {1}\nSkill: {2}\n", player1.Name, player1.Age, player1.Skill);

            Console.WriteLine("Player 2:");
            Console.WriteLine("Name: {0}\nAge: {1}\nSkill: {2}\n", player2.Name, player2.Age, player2.Skill);
        }
    }
}
