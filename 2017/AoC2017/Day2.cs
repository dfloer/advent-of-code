using System;
using System.Collections.Generic;
using System.Collections;

namespace Day2
{
    partial class Program
    {
        static void Main(string[] args)
        {
            string line;
            System.IO.StreamReader file = new System.IO.StreamReader(@"day2.txt");
            int pt1_checksum = 0;
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
                pt1_checksum += line_diff;
            }
            file.Close();
            System.Console.WriteLine("Day1, Part1 solution: {0}", pt1_checksum);
            int pt2_checksum = 0;

            file = new System.IO.StreamReader(@"day2.txt");
            while ((line = file.ReadLine()) != null)
            {
                List<int> int_list = new List<int>();
                string[] split_line = line.Split();
                foreach (string e in split_line)
                {
                    int n = int.Parse(e);
                    int_list.Add(n);
                }
                int line_length = int_list.Count;
                for(int i = 0; i < line_length; i++)
                {
                    for (int j = i + 1; j < line_length; j++)
                    {
                        int a = int_list[i];
                        int b = int_list[j];
                        if (a % b == 0)
                        {
                            pt2_checksum += a / b;
                            break;
                        }
                        if (b % a == 0)
                        {
                            pt2_checksum += b / a;
                            break;
                        }
                    }
                }
            }
            file.Close();
            System.Console.WriteLine("Day2, Part2 solution: {0}", pt2_checksum);

            // Keep console window open when we end.
            Console.WriteLine("Press any key to exit.");
            System.Console.ReadKey();
        }
    }
}
