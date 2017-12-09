using System;
using System.Collections.Generic;
using System.Linq;
using System.Collections.ObjectModel;

namespace Day9
{
    partial class Program
    {
        static void Main(string[] args)
        {
            string input_text = System.IO.File.ReadAllText(@"day9.txt");
            int idx = 0;
            var stack = new Stack<int>();
            bool garbage = false;
            int stack_sum = 0;
            int garbage_sum = 0;
            while (idx < input_text.Length)
            {
                char chr = input_text[idx];
                if (chr == '!')
                {
                    idx += 2;
                    continue;
                }
                else if (chr =='{' & !garbage)
                {
                    stack.Push(idx);
                }
                else if (chr == '}' & !garbage)
                {
                    stack_sum += stack.Count();
                    int new_idx = stack.Any() ? stack.Pop() : -1;             
                }
                else if (chr == '<' & !garbage)
                {
                    garbage = true;
                }
                else if (chr == '>' & garbage)
                {
                    garbage = false;
                }
                else if (garbage)
                {
                    garbage_sum++;
                }
                idx++;
            }
            System.Console.WriteLine("Solution to Day9 Part1: {0}", stack_sum);
            System.Console.WriteLine("Solution to Day9 Part2: {0}", garbage_sum);
        }
    }
}