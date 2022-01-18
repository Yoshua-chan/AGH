using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace game
{
    public class MonsterEntity : MapEntity

    {
        public List<Monster> content;
        public MonsterEntity()
        {
             this.content = new List<Monster>();
        }
        public MonsterEntity(Position pos)
        {
            this.content = new List<Monster>();
            this.position = pos;
        }
        public void MoveUp()
        {
            if (Map.mapArray[this.position.room, this.position.y - 1, this.position.x] != 1)
            {
                this.position.y -= 1;
            }
        }
        public void MoveDown()
        {
            if (Map.mapArray[this.position.room, this.position.y + 1, this.position.x] != 1)
            {
                this.position.y += 1;
            }
        }
        public void MoveLeft()
        {
            if (Map.mapArray[this.position.room, this.position.y, this.position.x - 1] != 1)
            {
                this.position.x -= 1;
            }
        }
        public void MoveRight()
        {
            if (Map.mapArray[this.position.room, this.position.y, this.position.x + 1] != 1)
            {
                this.position.x += 1;
            }
        }
        public void Move()
        {
            Random rnd = new Random();
            double value = rnd.NextDouble();
            if(value < 0.25)
            {
                this.MoveUp();
            } else if(value < 0.5)
            {
                this.MoveDown();
            } else if(value < 0.75)
            {
                this.MoveLeft();
            } else if(value < 1)
            {
                this.MoveRight();
            }
        }
        public bool CheckForPlayer(Player pl)
        {
            if( (pl.position.x == this.position.x - 1 || pl.position.x == this.position.x + 1 || pl.position.x == this.position.x) && 
                (pl.position.y == this.position.y - 1 || pl.position.y == this.position.y + 1 || pl.position.y == this.position.y))
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        /*
         * this.x = 8
         * this.y = 8;
         * 
         * pl.x = 7
         * pl.y = 9
         * */
   }
    
}
