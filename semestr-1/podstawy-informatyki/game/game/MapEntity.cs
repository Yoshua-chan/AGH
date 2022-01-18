using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace game
{
    public class MapEntity
    {
        public Position position;
        public MapEntity(Position pos)
        {
                this.position = pos;
        }
        public MapEntity()
        {
            this.position = new Position(0, 0, 0);
        }
    }
}
