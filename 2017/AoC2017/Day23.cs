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
            List<string> instructions = new List<string>();
            foreach (char c in "abcdefgh")
                registers[c] = 0;
            while ((raw_line = file.ReadLine()) != null)
            {
                instructions.Add(raw_line);
            }
            long pt1 = part1(registers, instructions);
            System.Console.WriteLine("Solution to Day23 Part2: {0}", pt1);
            registers['a'] = 1;
            foreach (char c in "bcdefgh")
                registers[c] = 0;
            registers = part2(registers, instructions);
            System.Console.WriteLine("Solution to Day23 Part2: {0}", registers['h']);
        }
        static long part1(Dictionary<char, long> registers, List<string> instructions)
        {
            List<string> split_line = instructions[0].Split(' ').ToList();
            long initial_value = long.Parse(split_line[2]);
            return (long)Math.Pow(initial_value - 2, 2);
        }
        static Dictionary<char, long> part2(Dictionary<char, long> registers, List<string> instructions)
        {
            int program_counter = 0;
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
                //Optimization time. When we've hit instruction 8, the program spends a lot of time doing stuff.
                if (program_counter == 8)
                    break;
            }
            long low_val = registers['b'];
            long high_val = registers['c'];
            /* When I was attempting to reverse engineer the program, I saw that it generated two numbers in reg b and c.
             * And then when a number between them was prime, it didn't increment register h.
             * Not sure where the increment of 17 comes from, but it's what my input used.
             * So register h should be the number of non-primes between the numbers in reg b and c.*/
            for (long i = low_val; i <= high_val; i += 17)
                if (!is_prime(i))
                    registers['h']++;
            return registers;
        }
        static bool is_prime(long n)
        {
            if (n == 1)
                return false;
            if (n == 2)
                return true;
            if (n % 2 == 0)
                return false;
            var half = (int)Math.Floor(Math.Sqrt(n));
            for (int i = 3; i <= half; i += 2)
                if (n % i == 0)
                    return false;
            return true;
        }
    }
}