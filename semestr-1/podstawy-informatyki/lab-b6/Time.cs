using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab_b6
{
    class Time
    {
        public int hours;
        public int minutes;
        public int seconds;
        public bool initialized;

        public Time(int hours, int minutes, int seconds)
        {
            this.hours = hours;
            this.minutes = minutes;
            this.seconds = seconds;
            this.initialized = true;
        }

        public Time()
        {
            this.hours = this.minutes = this.seconds = 0;
            this.initialized = false;
        }

        void Normalize()
        {
           
        }
        public string GetString()
        {
            Normalize();
            return String.Format("{0}:{1}:{2}", this.hours, this.minutes, this.seconds);
        }
    }

}
