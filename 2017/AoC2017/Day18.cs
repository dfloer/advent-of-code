using System;
using System.Collections.Generic;
using System.Linq;

namespace Day18
{
    partial class Program
    {
        static void Main(string[] args)
        {
            System.IO.StreamReader file = new System.IO.StreamReader(@"day18.txt");
            string raw_line;
            Dictionary<char, long> registers = new Dictionary<char, long>();
            Stack<long> freqs = new Stack<long>();
            List<string> instructions = new List<string>();
            int program_counter = 0;
            while ((raw_line = file.ReadLine()) != null)
            {
                instructions.Add(raw_line);
            }
            long pt1 = 0;
            while (program_counter < instructions.Count())
            {
                List<string> split_line = instructions[program_counter].Split(' ').ToList();
                string inst = split_line[0];
                char reg = split_line[1].ToCharArray()[0];
                // Basically, make this act like a Dictionary with a default value of 0.
                try
                {
                    var _ = registers[reg];
                }
                catch (KeyNotFoundException)
                {
                    registers[reg] = 0;
                }
                long value = -1;
                if (split_line.Count == 3)
                {
                    try
                    {
                        value = long.Parse(split_line[2]);
                    }
                    catch (FormatException)
                    {
                        char r = split_line[2].ToCharArray()[0];
                        value = registers[r];
                    }
                }
                int pc_offset = 1;
                switch (inst)
                {
                    case "snd":
                        freqs.Push(registers[reg]);
                        break;
                    case "set":
                        registers[reg] = value;
                        break;
                    case "add":
                        registers[reg] += value;
                        break;
                    case "mul":
                        registers[reg] *= value;
                        break;
                    case "mod":
                        registers[reg] %= value;
                        break;
                    case "rcv":
                        long x = registers[reg];
                        if (x != 0)
                        {
                            registers[reg] = freqs.Pop();
                            if (pt1 == 0)
                                pt1 = registers[reg];
                            pc_offset = 42424242; // For now, this will halt program execution.
                        }
                        break;
                    case "jgz":
                        long X = registers[reg];
                        if (X > 0)
                            pc_offset = (int)value;
                        break;
                }
                program_counter += pc_offset;
            }
            System.Console.WriteLine("Solution to Day18 Part1: {0}", pt1);
        }
    }
}