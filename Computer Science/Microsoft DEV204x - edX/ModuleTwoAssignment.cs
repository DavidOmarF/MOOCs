using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ModuleTwoAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
        
        // This code is very messy! Too many for and if it's not exactly good. 
        // I did it this way just because the point of the practice was using nested loops.
        
            for (int i = 0; i < 8; i++)
            {
                if (i % 2 == 0)
                {
                    for (int j = 0; j < 8; j++)
                    {
                        if (j % 2 == 0)
                        {
                            Console.Write("X");
                        }
                        else
                        {
                            Console.Write("O");
                        }
                    }
                    Console.Write("\n");
                }
                else
                {
                    for (int j = 0; j < 8; j++)
                    {
                        if (j % 2 == 0)
                        {
                            Console.Write("O");
                        }
                        else
                        {
                            Console.Write("X");
                        }
                    }
                    Console.Write("\n");
                }
            }
            Console.ReadLine();
        }
    }
}
