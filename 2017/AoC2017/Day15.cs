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
            int pairs_pt2 = 5000000;
            System.IO.StreamReader file = new System.IO.StreamReader(@"day15.txt");
            string raw_line = file.ReadLine();
            long a_seed = long.Parse(raw_line.Split(' ')[4]);
            raw_line = file.ReadLine();
            long b_seed = long.Parse(raw_line.Split(' ')[4]);
            int a_factor = 16807;
            int b_factor = 48271;
            int div = 2147483647;

            int count = 0;
            long a = a_seed;
            long b = b_seed;
            List<long> valid_a = new List<long>();
            List<long> valid_b = new List<long>();
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
            int count_pt2 = 0;
            a = a_seed;
            b = b_seed;
            while (valid_b.Count < pairs_pt2)
            {
                a = (a * a_factor) % div;
                b = (b * b_factor) % div;
                long a_lower16b = (a & 0xFFFF);
                long b_lower16b = (b & 0xFFFF);
                if (a_lower16b % 4 == 0)
                    valid_a.Add(a_lower16b);
                if (b_lower16b % 8 == 0)
                    valid_b.Add(b_lower16b);
            }
            foreach(int i in Enumerable.Range(0, valid_b.Count))
            {
                if (valid_a[i] == valid_b[i])
                    count_pt2++;
            }
            System.Console.WriteLine("Solution to Day15 Part2: {0}", count_pt2);
        }
    }
}