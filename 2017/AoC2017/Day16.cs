using System;
using System.Collections.Generic;
using System.Linq;

namespace Day16
{
    partial class Program
    {
        static void Main(string[] args)
        {
            System.IO.StreamReader file = new System.IO.StreamReader(@"day16.txt");
            List<string> dance_moves = file.ReadLine().Split(',').ToList();
            List<char> programs = new List<char>("abcdefghijklmnop".ToCharArray());
            foreach(string move in dance_moves)
            {
                char inst = move.First();
                /*System.Console.WriteLine(move);
                foreach (var x in programs)
                    System.Console.Write(x);
                System.Console.WriteLine("");*/
                switch (inst)
                {
                    case 's':
                        int num = int.Parse(move.Substring(1));
                        /*System.Console.WriteLine(num);
                        foreach (var x in programs)
                            System.Console.Write(x);
                        System.Console.WriteLine("");*/
                        programs = rotate(programs, num);
                        /*foreach (var x in programs)
                            System.Console.Write(x);
                        System.Console.WriteLine("");*/
                        break;
                    case 'x':
                        List<string> temp_x = move.Substring(1).Split('/').ToList();
                        int a_x = int.Parse(temp_x.First());
                        int b_x = int.Parse(temp_x.Last());
                        programs = swap_idx(programs, a_x, b_x);
                        break;
                    case 'p':
                        List<string> temp_p = move.Substring(1).Split('/').ToList();
                        int a_p = programs.IndexOf(Convert.ToChar(temp_p.First()));
                        int b_p = programs.IndexOf(Convert.ToChar(temp_p.Last()));
                        programs = swap_idx(programs, a_p, b_p);
                        break;
                }
            }
            System.Console.Write("Solution to Day16 Part1: ");
            // Because concatenating a list of chars in C# is apparently a hard problem.
            foreach (var x in programs)
                System.Console.Write(x);
            System.Console.WriteLine("");
        }
        // Rotates the list n places, that is, the last n elements move to the front.
        static List<char> rotate(List<char> l, int n)
        {
            char x;
            for (int i = 0; i < n; i++)
            {
                x = l[l.Count - 1];
                l.RemoveAt(l.Count - 1);
                l.Insert(0, x);
            }
            return l;
        }
        // Swaps the elements and the two indices with eath other.
        static List<char> swap_idx(List<char> l, int idx_a, int idx_b)
        {
            //System.Console.WriteLine("{0}, {1}", idx_a, idx_b);
            char temp = l[idx_a];
            l[idx_a] = l[idx_b];
            l[idx_b] = temp;
            return l;
        }
    }
}