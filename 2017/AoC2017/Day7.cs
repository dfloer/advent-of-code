using System;
using System.Collections.Generic;
using System.Linq;
using System.Collections.ObjectModel;

namespace Day7
{
    partial class Program
    {
        static void Main(string[] args)
        {
            string line;
            // Used to get counts of how many times a node was seen in the input, to find the root.
            List<string> all_nodes = new List<string>();
            // Used to map node keys to list indexes. Use a dictionary?
            List<string> node_keys = new List<string>();
            System.IO.StreamReader file = new System.IO.StreamReader(@"day7.txt");
            string root = "";
            List<Node> tree_nodes = new List<Node>();
            while ((line = file.ReadLine()) != null)
            {
                string[] temp = line.Split();
                string key = temp[0];
                int weight = int.Parse(temp[1].Substring(1, temp[1].Length - 2));
                all_nodes.Add(key);
                node_keys.Add(key);
                Node parent = new Node(key, weight);
                for (int i = 3; i < temp.Length; i += 1)
                {
                    string child_key = temp[i].TrimEnd(',');
                    Node child = new Node(child_key, 0);
                    child.parent = parent;
                    all_nodes.Add(child_key);
                    parent.child_values.Add(child_key);
                }
                tree_nodes.Add(parent);
            }
            // The root will only show up in the input exactly once.
            var g = all_nodes.GroupBy(i => i);
            foreach (var grp in g)
            {
                if (grp.Count() == 1)
                {
                    root = grp.Key;
                }
            }
            System.Console.WriteLine("Solution to day7 part1: {0}", root);
            // Now that we have all the nodes, we actually need to stitch them together into a tree.
            foreach (Node this_node in tree_nodes)
            {
                foreach(string child_id in this_node.child_values)
                {
                    int child_node_idx = node_keys.IndexOf(child_id);
                    Node child_node = tree_nodes[child_node_idx];
                    child_node.parent = this_node;
                    this_node.child_nodes.Add(child_node);
                }
            }
            int target_weight = 0;
            Node next_node = tree_nodes[node_keys.IndexOf(root)];
            while (next_node.check_balanced() == false)
            {
                (next_node, target_weight) = next_node.find_unbalanced_child();
            }
            int weight_difference = target_weight - next_node.get_subtree_weight();
            int weight_fudge = next_node.weight + weight_difference;
            System.Console.WriteLine("Solution to day7 part2: {0}", weight_fudge);
        }
    }
    public class Node
    {
        public string value { get; set; }
        public int weight { get; set; }
        public List<string> child_values { get; set; }
        public List<Node> child_nodes { get; set; }
        public Node parent { get; set; }

        public Node(string node_value, int node_weight)
        {
            value = node_value;
            weight = node_weight;
            child_values = new List<string>();
            child_nodes = new List<Node>();
            parent = null;
        }
        public bool check_balanced()
        {
            // Get the weights of all of the subtrees. One will be different than the others.
            var grp = child_nodes.GroupBy(i => i.get_subtree_weight());
            // Well, only different if it's unbalanced. If it's not different, we've found the bad node.
            return grp.Count() == 1;
        }
        public int get_subtree_weight()
        {
            // Recursively get the weights of all the children and sum them all together.
            int children_sum = child_nodes.Sum(x => x.get_subtree_weight());
            // And then add it to our running total.
            int total = children_sum + weight;
            return total;
        }
        public (Node node, int target_weight) find_unbalanced_child()
        {
            // Get the weights of all the subtrees. If one is different, it's unbalanced.
            var grp = child_nodes.GroupBy(i => i.get_subtree_weight());
            // The target weight is the weight the other nodes have.
            var target_weight = grp.First(i => i.Count() > 1).Key;
            // Get the node that corresponds to the unbalanced child.
            var child_unbalanced = grp.First(i => i.Count() == 1).First();
            return (child_unbalanced, target_weight);
        }
    }
}