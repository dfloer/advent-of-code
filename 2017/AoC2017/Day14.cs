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
            List<List<int>> grid = new List<List<int>>();
            foreach (int i in Enumerable.Range(0, 128))
            {
                string row_seed = input + "-" + i.ToString();
                string result = generate_knot_hash(hash_size, row_seed);
                string binary = hex_2_bin(result);
                List<int> line = binary.Select(x => int.Parse(x.ToString())).ToList();
                grid.Add(line);
            }
            int accum = 0;
            foreach (List<int> l in grid)
                accum += l.Sum();
            System.Console.WriteLine("Solution to Day14 Part1: {0}", accum);
            // Convert this into a problem like day 12.
            /*Dictionary<int, HashSet<int>> adjacency_list = new Dictionary<int, HashSet<int>>();
            foreach (int i in Enumerable.Range(0, 128))
            {
                foreach (int j in Enumerable.Range(0, 128))
                {
                    int idx = i * 128 + j;
                    List<int> adjacent = get_lower_adjacent(grid, i, j);
                    System.Console.WriteLine("i: {0}, j: {1}, adj: {2}, idx: {3}", i, j, adjacent.Count, idx);
                    if (adjacent.Count == 0)
                    {
                        HashSet<int> temp = new HashSet<int>();
                        temp.Add(idx);
                        adjacency_list[idx] = temp;
                    }
                    else
                    {
                        HashSet<int> temp = new HashSet<int>(adjacent);
                        adjacency_list[idx] = temp;
                    }
                }
            }
            int subgraphs = count_subgraphs(adjacency_list);*/
            int subgraphs = traverse_matrix(grid);
            System.Console.WriteLine("Solution to Day14 Part2: {0}", subgraphs);
        }
        // Copied more or less straight from my day10 solution.
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
        // Copied more or less straight from day12 solution.
        static HashSet<int> depth_first_search(Dictionary<int, HashSet<int>> adj, int start)
        {
            HashSet<int> connected = new HashSet<int>();
            Stack<int> stack = new Stack<int>();
            if (!adj.ContainsKey(start))
            {
                return connected;
            }
            stack.Push(start);
            while (stack.Count > 0)
            {
                int vert = stack.Pop();
                if (connected.Contains(vert))
                {
                    continue;
                }
                connected.Add(vert);
                foreach (int next in adj[vert])
                {
                    if (!connected.Contains(next))
                    {
                        stack.Push(next);
                    }
                }
            }
            return connected;
        }
        static int count_subgraphs(Dictionary<int, HashSet<int>> grid)
        {
            int subgraph_count = 0;
            int pt1 = 0;
            HashSet<int> all_connected = new HashSet<int>();
            while (all_connected.Count < grid.Count)
            {
                // This is a hashset containing all the unvisited nodes. Take the first node for DFS.
                HashSet<int> to_visit = new HashSet<int>(new HashSet<int>(grid.Keys).Except(all_connected));
                int root = to_visit.First();
                // This is a hashset of all the nodes connected to the root node.
                HashSet<int> connected = depth_first_search(grid, root);
                if (pt1 == 0)
                {
                    pt1 = connected.Count();
                }
                // Finally, we don't want to visit the node again if we've already done so.
                all_connected.UnionWith(connected);
                subgraph_count++;
            }
            return subgraph_count;
        }
        static List<int> get_lower_adjacent(List<List<int>> arr, int row, int column)
        {
            int rows = arr.Count();
            int columns = arr[0].Count();
            List<int> result = new List<int>();

            for (int j = row - 1; j <= row + 1; j++)
            {
                for (int i = column - 1; i <= column + 1; i++)
                {
                    // Will find all adjacent values.
                    if (i >= 0 && j >= 0 && i < columns && j < rows && !(j == row && i == column))
                    {
                        // This should filter out the diagonals.
                        if (!(((i == column + 1) && (j == row + 1)) || ((i == column - 1) && (j == row + 1)) || ((i == column + 1) && (j == row - 1)) || ((i == column - 1) && (j == row - 1))))
                        {
                            int val = arr[i][j];
                            if (val == 1)
                                result.Add(j * 128 + i);
                            System.Console.WriteLine("i: {0}, j: {1}, val: {2}, row: {3}, col: {4}", i, j, val, row, column);
                        }
                    }
                }
            }
            return result;
        }

        static int traverse_matrix(List<List<int>> matrix)
        {
            int counter = 0;
            HashSet<Tuple<int, int>> unvisited = new HashSet<Tuple<int, int>>();
            foreach (int x in Enumerable.Range(0, 128))
                foreach (int y in Enumerable.Range(0, 128))
                    unvisited.Add(new Tuple<int, int>(x, y));
            while (unvisited.Count() > 0)
            {
                Tuple<int, int> node = unvisited.First();
                int i = node.Item1;
                int j = node.Item2;
                System.Console.WriteLine("i: {0}, j: {1}, val: {2}, ", i, j, matrix[i][j]);
                if (matrix[i][j] == 1)
                {
                    counter++;
                    visit_node(matrix, i, j, unvisited);
                }
                else
                    unvisited.Remove(node);
            }
            return counter;
        }
        static void visit_node(List<List<int>> matrix, int i, int j, HashSet<Tuple<int, int>> unvisited)
        {
            Tuple<int, int> node = new Tuple<int, int>(i, j);
            if (unvisited.Contains(node))
            {
                unvisited.Remove(node);
                if (matrix[i][j] == 1)
                {
                    if (j > 1)
                        visit_node(matrix, i, j - 1, unvisited);
                    if (j < 128)
                        visit_node(matrix, i, j + 1, unvisited);
                    if (i > 1)
                        visit_node(matrix, i - 1, j, unvisited);
                    if (i < 128)
                        visit_node(matrix, i + 1, j, unvisited);
                }
            }
        }
    }
}