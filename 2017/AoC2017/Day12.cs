using System;
using System.Collections.Generic;
using System.Linq;

namespace Day12
{
    partial class Program
    {
        static void Main(string[] args)
        {
            System.IO.StreamReader file = new System.IO.StreamReader(@"day12.txt");
            string raw_line;
            Dictionary<int, HashSet<int>> pipes = new Dictionary<int, HashSet<int>>();
            while ((raw_line = file.ReadLine()) != null)
            {
                List<string> line = raw_line.Split(new string[] {" ", ", "}, StringSplitOptions.None).ToList();
                int src = int.Parse(line[0]);
                HashSet<int> dest = new HashSet<int>();
                for (int i = 2; i < line.Count; i++)
                {
                    dest.Add(int.Parse(line[i]));
                }
                pipes.Add(src, dest);
            }
            int subgraph_count = 0;
            int pt1 = 0;
            HashSet <int> all_connected = new HashSet<int>();
            while (all_connected.Count < pipes.Count)
            {
                // This is a hashset containing all the unvisited nodes. Take the first node for DFS.
                HashSet<int> to_visit = new HashSet<int>(new HashSet<int>(pipes.Keys).Except(all_connected));
                int root = to_visit.First();
                // This is a hashset of all the nodes connected to the root node.
                HashSet<int> connected = depth_first_search(pipes, root);
                if (pt1 == 0)
                {
                    pt1 = connected.Count();
                }
                // Finally, we don't want to visit the node again if we've already done so.
                all_connected.UnionWith(connected);
                subgraph_count++;
            }
            System.Console.WriteLine("Solution to Day12 Part1: {0}", pt1);
            System.Console.WriteLine("Solution to Day12 Part2: {0}", subgraph_count);
        }

        static HashSet<int> depth_first_search(Dictionary<int, HashSet<int>> adj, int start)
        {
            HashSet<int> connected = new HashSet<int>();
            Stack<int> stack = new Stack<int>();
            if (!adj.ContainsKey(start))
            {
                return connected;
            }
            stack.Push(start);
            while(stack.Count > 0)
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
    }
}
