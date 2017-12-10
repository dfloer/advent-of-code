using System;
using System.Collections.Generic;
using System.Linq;
using System.Collections.ObjectModel;

namespace Day10
{
    partial class Program
    {
        static void Main(string[] args)
        {
            int hash_size = 256;
            string input_text = System.IO.File.ReadAllText(@"day10.txt");
            List<string> split_input = input_text.Split(',').ToList();
            int posn = 0;
            int skip_size = 0;
            List<int> hash_list = Enumerable.Range(0, hash_size).ToList();
            foreach (int length in split_input.Select(int.Parse).ToList())
            {
                List <int> new_hash_list = split_list(hash_list, posn, length);
                hash_list = new_hash_list;
                posn = (posn + length + skip_size) % hash_size;
                skip_size++;
            }
            int result = hash_list[0] * hash_list[1];
            System.Console.WriteLine("Solution to Day10 Part1: {0}", result);
        }

        static List<int> split_list(List<int> input_list, int posn, int len)
        {
            int list_max = input_list.Count;
            List<int> input_copy = input_list.ToList();
            for(int i = 0; i < len; i++)
            {
                int idx = (posn + i) % list_max;
                int new_idx = (posn + len - i - 1) % list_max;
                int new_elem = input_copy[new_idx];
                input_list[idx] = new_elem;
            }
            return input_list;
        }
    }
}