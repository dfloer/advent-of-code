using System;
using System.Collections.Generic;
using System.Linq;

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

            var input_copy = inst.ToList();
            int part1_res = part1(inst);
            System.Console.WriteLine("Solution to Day5 Part2: {0}", part1_res);
            int part2_res = part2(input_copy);
            System.Console.WriteLine("Solution to Day5 Part2: {0}", part2_res);

        }
        static int part1(List<int> inst)
        {
            int inst_idx = 0;
            int step_count = 0;
            while (true)
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
                    break;
                }
            }
            return step_count;
        }

        static int part2(List<int> inst)
        {
            int inst_idx = 0;
            int step_count = 0;
            while (true)
            {
                try
                {
                    int offset = inst[inst_idx];
                    if (offset >= 3)
                    {
                        inst[inst_idx] -= 1;
                    }
                    else
                    {
                        inst[inst_idx] += 1;
                    }
                    inst_idx += offset;
                    step_count += 1;
                }
                catch (System.ArgumentOutOfRangeException)
                {
                    break;
                }
            }
            return step_count;
        }
    }
}
