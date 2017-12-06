using System;
using System.Collections.Generic;
using System.Linq;

namespace Day6
{
    partial class Program
    {
        static void Main(string[] args)
        {
            string input_text = System.IO.File.ReadAllText(@"day6.txt");
            string[] line = input_text.Split();
            List<int> blocks = new List<int>();
            List<int[]> previous_bank = new List<int[]> { };
            foreach (string e in line)
            {
                blocks.Add(int.Parse(e));
            }
            int pt1_cycles = 0;
            int pt2_loop_cycles = 0;
            while (true)
            {
                int index_max = blocks.IndexOf(blocks.Max());
                int max_value = blocks[index_max];

                int idx = index_max + 1;
                while(max_value > 0)
                {
                    blocks[index_max] = 0 ;
                    blocks[idx % blocks.Count] += 1;
                    idx += 1;
                    max_value -= 1;
                }
                int[] new_blocks = blocks.ToArray();
                if (previous_bank.Any(x => x.SequenceEqual(new_blocks)))
                {
                    pt1_cycles = previous_bank.Count + 1;
                    /* Why doesn't this work?
                    This should show me how long ago I saw this, but IndexOf returns -1. */
                    //pt2_loop_cycles = previous_bank.Count - previous_bank.IndexOf(new_blocks);
                    //pt2_loop_cycles = previous_bank.IndexOf(new_blocks);
                    int i = 0;
                    while (i < previous_bank.Count)
                    {
                        int[] x = previous_bank[i];
                        if (x.SequenceEqual(new_blocks))
                        {
                            break;
                        }
                        i++;
                    }
                    pt2_loop_cycles = previous_bank.Count - i;
                    break;
                }
                else
                {
                    previous_bank.Add(new_blocks);
                }
            }
            System.Console.WriteLine("Solution to Day6 Part1: {0}", pt1_cycles);
            System.Console.WriteLine("Solution to Day6 Part2: {0}", pt2_loop_cycles);
        }
    }
}
