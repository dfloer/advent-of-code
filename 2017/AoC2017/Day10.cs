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
            List<int> lens_list = new List<int>();
            foreach(string l in split_input)
            {
                lens_list.Add(int.Parse(l));
            }
            int posn = 0;
            int skip_size = 0;
            List<int> hash_list = new List<int>(Enumerable.Range(0, hash_size));
            (hash_list, posn, skip_size) = pt1_round(lens_list, hash_list, posn, skip_size);            
            int result = hash_list[0] * hash_list[1];
            System.Console.WriteLine("Solution to Day10 Part1: {0}", result);

            // Change input file into int representation of each ASCII character.
            char[] lengths = input_text.ToCharArray();
            var len_bytes = System.Text.Encoding.ASCII.GetBytes(lengths);
            List<int> pt2_len_list = new List<int>();
            foreach(var len in len_bytes)
            {
                pt2_len_list.Add(Convert.ToInt32(len));
            }
            int[] extra_array = {17, 31, 73, 47, 23};
            List<int> extra = new List<int>(extra_array);
            pt2_len_list.AddRange(extra);

            // Do 64 rounds like in part1.
            posn = 0;
            skip_size = 0;
            hash_list = new List<int>(Enumerable.Range(0, hash_size));
            for (int i = 0; i < 64; i++)
            {
                (hash_list, posn, skip_size) = pt1_round(pt2_len_list, hash_list, posn, skip_size);
            }
            // Xor the 16 number blocks together to get the dense hash.
            List<int> sparse_hash = hash_list.ToList();
            List<int> dense_hash = new List<int>();
            for (int i = 0; i < hash_size; i+=16)
            {
                List<int> hash_block = sparse_hash.Skip(i).Take(16).ToList();
                int accumulator = 0;
                foreach(int v in hash_block)
                {
                    accumulator ^= v;
                }
                dense_hash.Add(accumulator);
            }
            // Finally convert the numbers to their hex representation.
            string dense_hash_hex = "";
            foreach(int h in dense_hash)
            {
                dense_hash_hex += h.ToString("X");
            }
            System.Console.WriteLine("Solution to Day10 Part2: {0}", dense_hash_hex);
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

        static Tuple<List<int>, int, int> pt1_round(List<int> length_list, List<int> hash_list, int posn, int skip_size)
        {
            int hash_size = hash_list.Count();
            foreach (int length in length_list)
            {
                List<int> new_hash_list = split_list(hash_list, posn, length);
                hash_list = new_hash_list;
                posn = (posn + length + skip_size) % hash_size;
                skip_size++;
            }
            Tuple <List<int>, int, int>  result = new Tuple<List<int>, int, int>(hash_list, posn, skip_size);
            return result;
        }

    }
}