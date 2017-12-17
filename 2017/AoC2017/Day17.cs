using System;
using System.Collections.Generic;
using System.Linq;

namespace Day17
{
    partial class Program
    {
        static void Main(string[] args)
        {
            int input = 312;
            int circular_len = 2017;
            List<int> spinlock = new List<int>();
            int pos_idx = 0;
            spinlock.Add(0);

            foreach(int i in Enumerable.Range(1, circular_len))
            {
                pos_idx = ((pos_idx + input) % spinlock.Count) + 1;
                spinlock.Insert(pos_idx, i);                
            }
            int pt1 = spinlock[spinlock.IndexOf(2017) + 1];
            System.Console.Write("Solution to Day17 Part1: {0}", pt1);
        }
    }
}