using System;
using System.Collections.Generic;
using System.Linq;

namespace Day14
{
    partial class Program
    {
        static void Main(string[] args)
        {
            int hash_size = 256;
            string input = "ljoxqyyw";
            int used_count = 0;
            foreach (int i in Enumerable.Range(0, 128))
            {
                string row_seed = input + "-" + i.ToString();
                string result = generate_knot_hash(hash_size, row_seed);
                // Split the string into pieces because C# is stupid and doesn't have arbitrary length ints.
                for (int j = 0; j < 32; j += 8)
                {
                    string to_convert = result.Substring(j, 8);
                    uint temp = uint.Parse(to_convert, System.Globalization.NumberStyles.HexNumber);
                    used_count += pop_count(temp);
                }
            }
            System.Console.WriteLine("Solution to Day12 Part1: {0}", used_count);
            //System.Console.WriteLine("Solution to Day12 Part2: {0}", pt2);
        }

        static string generate_knot_hash(int hash_size, string input_string)
        {
            char[] lengths = input_string.ToCharArray();
            var len_bytes = System.Text.Encoding.ASCII.GetBytes(lengths);
            List<int> len_list = new List<int>();
            foreach (var len in len_bytes)
            {
                len_list.Add(Convert.ToInt32(len));
            }
            int[] extra_array = { 17, 31, 73, 47, 23 };
            List<int> extra = new List<int>(extra_array);
            len_list.AddRange(extra);
            return knot_hash(hash_size, len_list);
        }
        static string knot_hash(int hash_size, List<int> len_list)
        {
            int posn = 0;
            int skip_size = 0;
            List<int> hash_list = new List<int>(Enumerable.Range(0, hash_size));
            for (int i = 0; i< 64; i++)
            {
                (hash_list, posn, skip_size) = pt1_round(len_list, hash_list, posn, skip_size);
            }
            // Xor the 16 number blocks together to get the dense hash.
            List<int> sparse_hash = hash_list.ToList();
            List<int> dense_hash = new List<int>();
            for (int i = 0; i<hash_size; i+=16)
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
                dense_hash_hex += h.ToString("X2");
            }
            return dense_hash_hex;
        }
        static List<int> split_list(List<int> input_list, int posn, int len)
        {
            int list_max = input_list.Count;
            List<int> input_copy = input_list.ToList();
            for (int i = 0; i < len; i++)
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
            Tuple<List<int>, int, int> result = new Tuple<List<int>, int, int>(hash_list, posn, skip_size);
            return result;
        }
        static string hex_2_bin(string hex_string)
        {
            string binary_string = String.Join(String.Empty, hex_string.Select(c => Convert.ToString(Convert.ToInt32(c.ToString(), 16), 2).PadLeft(4, '0')));
            return binary_string;
        }
        static int pop_count(uint value)
        {
            value = value - ((value >> 1) & 0x55555555);
            value = (value & 0x33333333) + ((value >> 2) & 0x33333333);
            value = ((value + (value >> 4) & 0xF0F0F0F) * 0x1010101) >> 24;
            return unchecked((int)value);
        }
    }
}