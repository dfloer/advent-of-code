using System;
using System.Collections.Generic;
using System.Linq;

namespace Day23
{
    partial class Program
    {
        static void Main(string[] args)
        {
            System.IO.StreamReader file = new System.IO.StreamReader(@"day23.txt");
            string raw_line;
            Dictionary<char, long> registers = new Dictionary<char, long>();
            Stack<long> freqs = new Stack<long>();
            List<string> instructions = new List<string>();
            foreach (char c in "abcdefgh")
                registers[c] = 0;
            while ((raw_line = file.ReadLine()) != null)
            {
                instructions.Add(raw_line);
            }
            int program_counter = 0;
            long pt1_mul_count = 0;
            while (program_counter < instructions.Count())
            {
                List<string> split_line = instructions[program_counter].Split(' ').ToList();
                string inst = split_line[0];
                char reg = split_line[1].ToCharArray()[0];
                long value = -1;
                try
                {
                    value = long.Parse(split_line[2]);
                }
                catch (FormatException)
                {
                    char r = split_line[2].ToCharArray()[0];
                    value = registers[r];
                }
                int pc_offset = 1;
                switch (inst)
                {
                    case "set":
                        registers[reg] = value;
                        break;
                    case "sub":
                        registers[reg] -= value;
                        break;
                    case "mul":
                        registers[reg] *= value;
                        pt1_mul_count++;
                        break;
                    case "jnz":
                        long X = 1;
                        if (reg != '1')
                            X = registers[reg];
                        if (X != 0)
                        pc_offset = (int)value;
                        break;
                }
                program_counter += pc_offset;
            }
            System.Console.WriteLine("Solution to Day23 Part2: {0}", pt1_mul_count);
        }
    }
}