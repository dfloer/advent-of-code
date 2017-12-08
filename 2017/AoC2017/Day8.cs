using System;
using System.Collections.Generic;
using System.Linq;

namespace Day7
{
    partial class Program
    {
        static void Main(string[] args)
        {
            System.IO.StreamReader file = new System.IO.StreamReader(@"day8.txt");
            string raw_line;
            Dictionary<string, int> register_file = new Dictionary<string, int>();
            while ((raw_line = file.ReadLine()) != null)
            {
                List<string> line = raw_line.Split().ToList();
                string dest_reg = line[0];
                string oper = line[1];
                int value = int.Parse(line[2]);
                string comp_reg_key = line[4];
                string comparison = line[5];
                int comparison_value = int.Parse(line[6]);
                // This would be way easier with a DefaultDict.
                int comp_reg_value = 0;
                try
                {
                    comp_reg_value = register_file[comp_reg_key];
                }
                catch (System.Collections.Generic.KeyNotFoundException)
                {
                    register_file[comp_reg_key] = 0;
                }
                int dest_reg_value = 0;
                try
                {
                    dest_reg_value = register_file[dest_reg];
                }
                catch (System.Collections.Generic.KeyNotFoundException)
                {
                    register_file[dest_reg] = 0;
                }
                int amount = 0;
                // I'm not sure if C# has a comparison library like Python's Operator. I couldn't find one.
                if (comparison == "==")
                {
                    if (comp_reg_value == comparison_value)
                    {
                        amount = value;
                    }
                }
                else if (comparison == "!=")
                {
                    if (comp_reg_value != comparison_value)
                    {
                        amount = value;
                    }
                }
                else if (comparison == "<=")
                {
                    if (comp_reg_value <= comparison_value)
                    {
                        amount = value;
                    }
                }
                else if (comparison == ">=")
                {
                    if (comp_reg_value >= comparison_value)
                    {
                        amount = value;
                    }
                }
                else if (comparison == "<")
                {
                    if (comp_reg_value < comparison_value)
                    {
                        amount = value;
                    }
                }
                else if (comparison == ">")
                {
                    if (comp_reg_value > comparison_value)
                    {
                        amount = value;
                    }
                }
                else
                {
                    // This case should never be hit, but it's nice to have just in case.
                    System.Console.WriteLine("Bad comparison {0}", comparison);
                }
                if (oper == "dec")
                {
                    amount = -1 * amount;
                }
                register_file[dest_reg] += amount;
            }
            var reg_values = register_file.Values.ToList();
            reg_values.Sort();
            System.Console.WriteLine("Solution to Day8 Part1: {0}", reg_values[reg_values.Count - 1]);
        }
    }
}
