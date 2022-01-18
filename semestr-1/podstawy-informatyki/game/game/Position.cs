using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace game
{
    public class Position
    {
        public int room;
        public int x;
        public int y;
        public Position(int room, int x, int y)
        {
            this.room = room;
            this.x = x;
            this.y = y;
        }
    }
}
