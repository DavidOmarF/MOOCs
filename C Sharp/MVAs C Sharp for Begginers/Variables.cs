using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Variables
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("¿Cuál es tu nombre?");
            Console.Write("Escribe tu nombre: ");
            string miNombre;
            miNombre = Console.ReadLine();
            Console.Write("Escribe tu apellido: ");
            string miApellido;
            miApellido = Console.ReadLine();

            Console.WriteLine("Hola, " + miNombre + " " + miApellido + ", ¿Qué edad tienes?");

            Console.Write("Escribe tu edad: ");
            int miEdad;
            miEdad = Convert.ToInt32(Console.ReadLine());

            if (miEdad > 18)
            {
                Console.WriteLine("¡Vaya!, ya estás envejeciendo, " + miNombre);
            } else
            {
                Console.WriteLine("Eres aún muy pequeño, " + miNombre);
            }

            Console.ReadLine();
        }
    }
}
