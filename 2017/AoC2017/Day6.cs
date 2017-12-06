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
            //HashSet<int[]> previous_bank = new HashSet<int[]>();
            List<int[]> previous_bank = new List<int[]> { };
            foreach (string e in line)
            {
                blocks.Add(int.Parse(e));
            }
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
                // Why does this HashSet comparison never actually compare?
                //if (previous_bank.Contains(new_blocks))
                if (previous_bank.Any(x => x.SequenceEqual(new_blocks)))
                {
                    break;
                }
                else
                {
                    previous_bank.Add(new_blocks);
                }
            }
            System.Console.WriteLine("Solution to Day6 Part1: {0}", previous_bank.Count + 1);
        }
    }
}
