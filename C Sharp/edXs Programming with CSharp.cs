using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ModuleOneAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            string firstName;
            string lastName;
            DateTime birthDate;
            string addressLine1;
            string addressLine2;
            string city;
            string stateProvince;
            int postalCode;
            string country;

            Console.WriteLine("What's your first name?");
            //firstName = Console.ReadLine();

            Console.WriteLine("What's your last name?");
            //lastName = Console.ReadLine();

            Console.WriteLine("What's your Birth Date? (Use AAAA/MM/DD)");
            birthDate = Convert.ToDateTime(Console.ReadLine());

            Console.Write("Your address line 1: ");
            addressLine1 = Console.ReadLine();

            Console.Write("Your address line 2: ");
            addressLine2 = Console.ReadLine();

            Console.Write("City: ");
            city = Console.ReadLine();

            Console.Write("State or province: ");
            stateProvince = Console.ReadLine();

            Console.Write("ZIP or Postal Code: ");
            postalCode = Convert.ToInt32(Console.ReadLine());

            Console.Write("Country: ");
            country = Console.ReadLine();

            Console.WriteLine("Hi, " + 
                firstName +
                " " +
                lastName + 
                "!");

            Console.WriteLine(birthDate);

            Console.WriteLine("So, I bet you have " + 
                DateTime.Now.Subtract(birthDate).Days + 
                " days alive, right?");

            Console.ReadLine();

            Console.WriteLine("Don't worry, that's just " +
                Convert.ToInt32(DateTime.Now.Subtract(birthDate).Days) / 365 +
                " years.");
            
            Console.ReadLine();
        }
    }
}
