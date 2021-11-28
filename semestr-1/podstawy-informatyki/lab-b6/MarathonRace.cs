using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab_b6
{
    class MarathonRace
    {
        private string forename;
        private string lastname;
        public float RunTime;

        public static float BestTime = 0;

        public string Forename {
            get
            {
                return new string(this.forename);
            }
            set
            {
                this.forename = new string(value);
            }
        }

        public string Lastname
        {
            get
            {
                return new string(this.lastname);
            }
            set
            {
                this.lastname = new string(value);
            }
        }

        public MarathonRace(string forename, string lastname, int time)
        {
            this.Forename = forename;
            this.Lastname = lastname;
            this.RunTime = time;
            if(this.RunTime < BestTime || BestTime == 0) {
                BestTime = this.RunTime;
            }
        }

        public MarathonRace(MarathonRace race)
        {
            this.Forename = race.forename;
            this.Lastname = race.lastname;
            this.RunTime = race.RunTime;
        }
    }
}
