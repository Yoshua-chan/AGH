using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;

namespace GS
{
    class Program
    {
        static void Main(string[] args)
        {
            GradeSheet original = new GradeSheet("Jan Kowalski", GradeSheet.Groups.advanced);
            original.grades.Add("Język polski", 3.0);
            original.grades.Add("Matematyka", 4.5);
            original.grades.Add("Język angielski", 5);

            Console.WriteLine(original.grades["Język polski"]);
            Console.WriteLine(original.grades["Matematyka"]);
            Console.WriteLine(original.grades["Język angielski"]);
            Console.WriteLine(original.AvarageGrade());

            original.Serialize("./gradesheet.json");

            GradeSheet copy = GradeSheet.Deserialize("./gradesheet.json");
            //Console.WriteLine(copy.group);
        }
    }
}
