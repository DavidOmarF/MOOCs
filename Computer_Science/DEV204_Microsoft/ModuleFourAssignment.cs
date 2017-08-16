using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ModuleFourAssignment
{
    class Program
    {

        public struct Student
        {
            public Student(
                string firstName,
                string lastName,
                DateTime birthdate,
                string address1,
                string address2,
                string city,
                string state,
                int zip,
                string country)
            {
                this.firstName = firstName;
                this.lastName = lastName;
                this.birthdate = birthdate;
                this.address1 = address1;
                this.address2 = address2;
                this.city = city;
                this.state = state;
                this.zip = zip;
                this.country = country;
            }
            
            public string firstName;
            public string lastName;
            public DateTime birthdate;
            public string address1;
            public string address2;
            public string city;
            public string state;
            public int zip;
            public string country;
        }

        public struct Teacher
        {
            public Teacher(
                   string firstName,
                   string lastName,
                   DateTime birthdate,
                   string address1,
                   string address2,
                   string city,
                   string state,
                   int zip,
                   string country)
            {
                this.firstName = firstName;
                this.lastName = lastName;
                this.birthdate = birthdate;
                this.address1 = address1;
                this.address2 = address2;
                this.city = city;
                this.state = state;
                this.zip = zip;
                this.country = country;
            }
            public string firstName;
            public string lastName;
            public DateTime birthdate;
            public string address1;
            public string address2;
            public string city;
            public string state;
            public int zip;
            public string country;
        }

        public struct UProgram
        {
            public UProgram(
                string name,
                string departmentHead,
                string degrees)
            {
                this.name = name;
                this.departmentHead = departmentHead;
                this.degrees = degrees;
            }
            public string name;
            public string departmentHead;
            public string degrees;
        }

        public struct Course
        {
            public Course(
                string name,
                int credits,
                int duration,
                string teacher)
            {
                this.name = name;
                this.credits = credits;
                this.duration = duration;
                this.teacher = teacher;
            }
            public string name;
            public int credits;
            public int duration;
            public string teacher;
        }

        static void Main(string[] args)
        {
            Student[] studentsList = new Student[5];

            studentsList[0] = new Student(
                "David Omar",
                "Flores Chávez",
                Convert.ToDateTime("1998/10/25"), 
                "Tulipanes No. 34", 
                "Col. La Marmota Veloz", 
                "Zócalo", 
                "Ciudad de México", 
                56700, 
                "México");

            Console.WriteLine("Student No. 1 Info");

            Console.WriteLine("\nStudent's name: " +
                studentsList[0].firstName +
                " " +
                studentsList[0].lastName);

            Console.WriteLine("Birthdate : " +
                studentsList[0].birthdate.ToShortDateString());

            Console.WriteLine("Address: {0}, {1}, {2}, {3}, {4}",
                studentsList[0].address1,
                studentsList[0].address2,
                studentsList[0].city,
                studentsList[0].state,
                studentsList[0].country);
            
            Console.WriteLine("ZIP Code: " +
                studentsList[0].zip);


            Console.ReadLine();

        }
    }
}
