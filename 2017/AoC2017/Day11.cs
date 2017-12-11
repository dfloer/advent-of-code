using System;
using System.Collections.Generic;
using System.Linq;

namespace Day11
{
    partial class Program
    {
        static void Main(string[] args)
        {
            string input_text = System.IO.File.ReadAllText(@"day11.txt");
            List<string> split_input = input_text.Split(',').ToList();
            //Flat topped hexes.
            int x = 0;
            int y = 0;
            int z = 0;
            foreach(string dir in split_input)
            {
                switch (dir)
                {
                    case "n":
                        y++;
                        z--;
                        break;
                    case "s":
                        y--;
                        z++;
                        break;
                    case "sw":
                        x--;
                        z++;
                        break;
                    case "se":
                        x++;
                        y--;
                        break;
                    case "ne":
                        x++;
                        z--;
                        break;
                    case "nw":
                        x--;
                        y++;
                        break;
                }                        
            }
            int steps = (Math.Abs(x) + Math.Abs(y) + Math.Abs(z)) / 2;
            System.Console.WriteLine("Solution to Day11 Part1: {0}", steps);
            //System.Console.WriteLine("Solution to Day11 Part2: {0}", );
        }
    }
}
