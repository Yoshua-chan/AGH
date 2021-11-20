using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Chess
{
    class ChessPlayer
    {

        private int age;
        private int skill;
        private string name;

        public ChessPlayer(string name, int skill, int age)
        {
            this.Name = name;
            this.Age = age;
            this.Skill = skill;
        }

        public int Skill
        {
            get { return this.skill; }
            set { this.skill = value; }
        }

        public int Age
        {
            get { return this.age; }
            set
            {
                if (value < 100 && value > 5)
                    this.age = value;
            }
        }

        public string Name
        {
            get { return this.name; }
            set
            {
                if (value.Length < 25)
                {
                    this.name = value;
                }
            }
        }

        public void printAll()
        {
            Console.WriteLine("Name: {0}\nAge: {1}\nSkill: {2}\n", this.name, this.Age, this.skill);
        }
    }
}
