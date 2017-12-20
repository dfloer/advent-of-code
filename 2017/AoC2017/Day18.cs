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
                            //registers[reg] = freqs.Pop();
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
            List<long> to_sort = freqs.ToList();
            System.Console.WriteLine("Solution to Day18 Part1: {0}", to_sort[0]);
            /* Algorithm implements bubble sort.
             * It takes the numbers generated initially and then reverse sorts them.
             * The answer ends up being the number of iterations of bubble sort, divided by two (because two programs doing the work)
             * multiplied by the number of elements to get the total number of times a number would have been passed between the two.*/
            int iters = 1;
            bool swapped = false;
            while(true)
            {
                swapped = false;
                for (int i = to_sort.Count() - 1; i > 0; i--)
                {
                    long a = to_sort[i];
                    long b = to_sort[i - 1];
                    if(b > a)
                    {
                        to_sort[i] = b;
                        to_sort[i - 1] = a;
                        swapped = true;
                    }
                }
                iters++;
                if (!swapped)
                    break;
            }
            long pt2 = (iters / 2) * to_sort.Count();
            System.Console.WriteLine("Solution to Day18 Part2: {0}", pt2);
        }
    }
}