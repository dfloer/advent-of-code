using System;

namespace Day2
{
    partial class Program
    {
        static void Main(string[] args)
        {
            string line;
            System.IO.StreamReader file = new System.IO.StreamReader(@"day2.txt");
            int checksum = 0;
            while ((line = file.ReadLine()) != null)
            {
                int line_max = 0;
                int line_min = 10000000;
                string[] split_line = line.Split();
                foreach (string e in split_line)
                {
                    int n = int.Parse(e);
                    if (line_max < n)
                    {
                        line_max = n;
                    }
                    if (line_min > n)
                    {
                        line_min = n;
                    }
                }
                int line_diff = line_max - line_min;
                checksum += line_diff;
            }
            file.Close();
            System.Console.WriteLine("Day1, Part1 solution: {0}", checksum);
            // Keep console window open when we end.
            Console.WriteLine("Press any key to exit.");
            System.Console.ReadKey();
        }
    }
}
