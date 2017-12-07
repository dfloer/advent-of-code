using System;
using System.Collections.Generic;
using System.Linq;

namespace Day7
{
    partial class Program
    {
        static void Main(string[] args)
        {
            string line;
            List<string> all_nodes = new List<string>();
            System.IO.StreamReader file = new System.IO.StreamReader(@"day7.txt");
            while ((line = file.ReadLine()) != null)
            {
                string[] temp = line.Split();
                string key = temp[0];
                int weight = int.Parse(temp[1].Substring(1, temp[1].Length - 2));
                all_nodes.Add(key);
                for (int i = 3; i < temp.Length; i += 1)
                {
                    string child_key = temp[i].TrimEnd(',');
                    all_nodes.Add(child_key);
                }
            }
            // The root will only show up in the input exactly once.
            var g = all_nodes.GroupBy(i => i);
            foreach (var grp in g)
            {
                if (grp.Count() == 1)
                {
                    System.Console.WriteLine("Solution to day7 part1: {0}",grp.Key);
                }
            }
        }
    }
}
