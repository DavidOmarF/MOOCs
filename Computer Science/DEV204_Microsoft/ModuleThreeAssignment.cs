using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MethodsAndExceptions
{
    class Program
    {
        static void Main(string[] args)
        {
            //StudentBirthDateValidation();
            #region Student

            getStudentInfo(
                out string studentFirstName,
                out string studentLastName,
                out DateTime studentBirthdate);

            printStudentInfo(
                studentFirstName,
                studentLastName,
                studentBirthdate);

            #endregion

            #region Teacher

            GetTeacherInfo(
                out string teacherFirstName,
                out string teacherLastName,
                out DateTime teacherBirthdate);
            PrintTeacherInfo(
                teacherFirstName,
                teacherLastName,
                teacherBirthdate);

            #endregion

            #region UProgram

            GetUProgramInfo(
            out string programName,
            out string departmentHead,
            out string programDegrees);

            PrintUProgramInfo(
                programName,
                departmentHead,
                programDegrees);

            #endregion

            #region Degree
            GetDegreeInfo(
                out string degreeName,
                out int creditsRequired);
            PrintDegreeInfo(
                degreeName,
                creditsRequired);
#endregion
        }

        #region Student

        static void getStudentInfo(
            out string studentFirstName,
            out string studentLastName,
            out DateTime studentBirthdate)
        {
            Console.Write("Student's first name: ");
            studentFirstName = Console.ReadLine();

            Console.Write("Student's last name: ");
            studentLastName = Console.ReadLine();

            Console.Write("Birthdate: ");
            studentBirthdate = Convert.ToDateTime(Console.ReadLine());
        }

        static void printStudentInfo(
            string studentFirstName,
            string studentLastName,
            DateTime studentBirthdate)
        {
            Console.WriteLine("{1} {0} was born in {2}",
                studentFirstName,
                studentLastName,
                studentBirthdate.ToShortDateString());
        }
        #endregion

        #region Teacher

        static void GetTeacherInfo(
            out string teacherFirstName,
            out string teacherLastName,
            out DateTime teacherBirthdate)
        {
            Console.Write("Teacher's first name: ");
            teacherFirstName = Console.ReadLine();

            Console.Write("Teacher's last name: ");
            teacherLastName = Console.ReadLine();

            Console.Write("Birthdate: ");
            teacherBirthdate = Convert.ToDateTime(Console.ReadLine()); 
        }

        static void PrintTeacherInfo(
            string teacherFirstName,
            string teacherLastName,
            DateTime teacherBirthdate)
        {
            Console.WriteLine("{1} {0} was born in {2}",
                teacherFirstName,
                teacherLastName,
                teacherBirthdate.ToShortDateString());
        }
        #endregion

        #region UProgram

        static void GetUProgramInfo(
            out string programName,
            out string departmentHead,
            out string programDegrees)
        {
            Console.Write("Program's name: ");
            programName = Console.ReadLine();

            Console.Write("Program's department head: ");
            departmentHead = Console.ReadLine();

            Console.Write("Program degrees: ");
            programDegrees = Console.ReadLine();
        }

        static void PrintUProgramInfo(
            string programName,
            string departmentHead,
            string programDegrees)
        {
            Console.WriteLine("{0} program is under {1} department and offers {2} degree",
                programName,
                departmentHead,
                programDegrees);
        }
        #endregion

        #region Degree
        static void GetDegreeInfo(
                out string degreeName,
                out int creditsRequired)
        {
            Console.Write("Degree's name: ");
            degreeName = Console.ReadLine();

            Console.Write("Credits required: ");
            creditsRequired = Convert.ToInt32(Console.ReadLine());
        }

        static void PrintDegreeInfo(
            string degreeName,
            int creditsRequired)
        {
            Console.WriteLine("{0} degree requires {1}",
                degreeName,
                creditsRequired);
        }
        #endregion

        static void StudentBirthDateValidation()
        {
            throw new NotImplementedException();
        }

    }
}
