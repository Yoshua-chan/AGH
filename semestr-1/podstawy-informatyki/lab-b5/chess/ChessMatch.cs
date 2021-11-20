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
    }
}
