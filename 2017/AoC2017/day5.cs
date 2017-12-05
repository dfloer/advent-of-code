using System;
using System.Collections.Generic;


namespace Day5
{
    partial class Program
    {
        static void Main(string[] args)
        {
            string line;
            List<int> inst = new List<int>();
            System.IO.StreamReader file = new System.IO.StreamReader(@"day5.txt");
            while ((line = file.ReadLine()) != null)
            {
                int value = int.Parse(line);
                inst.Add(value);
            }
            
            int inst_idx = 0;
            int step_count = 0;
            while(true)
            {
                try
                {
                    int offset = inst[inst_idx];
                    inst[inst_idx] = offset + 1;
                    inst_idx += offset;
                    step_count += 1;
                }
                catch (System.ArgumentOutOfRangeException)
                {
                    System.Console.WriteLine("Solution to Day5 Part1: {0}", step_count);
                    break;
                }
            }
        }
    }
}
