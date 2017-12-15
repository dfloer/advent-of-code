using System;
using System.Collections.Generic;
using System.Linq;

namespace Day15
{
    partial class Program
    {
        static void Main(string[] args)
        {
            int iterations = 40000000;
            System.IO.StreamReader file = new System.IO.StreamReader(@"day15.txt");
            string raw_line = file.ReadLine();
            long a = long.Parse(raw_line.Split(' ')[4]);
            raw_line = file.ReadLine();
            long b = long.Parse(raw_line.Split(' ')[4]);
            int a_factor = 16807;
            int b_factor = 48271;
            int div = 2147483647;

            int count = 0;
            foreach (int i in Enumerable.Range(0, iterations))
            {
                a = (a * a_factor) % div;
                b = (b * b_factor) % div;
                long a_lower16b = (a & 0xFFFF);
                long b_lower16b = (b & 0xFFFF);
                if (a_lower16b == b_lower16b)
                    count++;
            }
            System.Console.WriteLine("Solution to Day15 Part1: {0}", count);
            //System.Console.WriteLine("Solution to Day15 Part2: {0}", pt2);
        }
    }
}