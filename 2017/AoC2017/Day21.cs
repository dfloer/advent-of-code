using System;
using System.Collections.Generic;
using System.Linq;

namespace Day21
{
    partial class Program
    {
        static void Main(string[] args)
        {
            System.IO.StreamReader file = new System.IO.StreamReader(@"day21.txt");
            string raw_line;
            int iters = 5;
            Dictionary<List<string>, List<string>> rules = new Dictionary<List<string>, List<string>>();
            List<string> grid = new List<string>();
            grid.Add(".#.".ToString());
            grid.Add("..#".ToString());
            grid.Add("###".ToString());
            int xxx = 0;
            while ((raw_line = file.ReadLine()) != null)
            {
                List<string> temp = raw_line.Replace(" ", String.Empty).Split(new string[] { "=>" }, StringSplitOptions.None).ToList();
                string first = temp.First();
                string last = temp.Last();
                List<string> match_rule = parse_rule(first);
                List<string> rule_result = parse_rule(last);
                rules[match_rule] = rule_result;
                //Handle the 3 rotations and 2 flips right now.
                List<string> rotate_90 = rotate(match_rule); // Doesn't rotate. ???
                List<string> rotate_180 = rotate(rotate_90); // Actually 90.
                List<string> rotate_270 = rotate(rotate_180); // actually 180.
                //List<string> rotate_360 = rotate(rotate_270); // Actually 270.
                List<string> flip_vertical = flip_vert(match_rule);
                List<string> flip_horizontal = flip_horiz(match_rule);
                rules[rotate_90] = rule_result;
                rules[rotate_180] = rule_result;
                rules[rotate_270] = rule_result;
                //rules[rotate_360] = rule_result;
                rules[flip_vertical] = rule_result;
                rules[flip_horizontal] = rule_result;
                if (grid.SequenceEqual(match_rule) || grid.SequenceEqual(rotate_90)
                    || grid.SequenceEqual(rotate_180) || grid.SequenceEqual(rotate_270)
                    /*|| grid.SequenceEqual(rotate_360)*/ || grid.SequenceEqual(flip_vertical)
                    || grid.SequenceEqual(flip_horizontal) || xxx == 47)
                {
                    System.Console.WriteLine("Result at {0}: ", xxx);
                    print_array(rule_result);
                    System.Console.WriteLine("Match:");
                    print_array(match_rule);
                    System.Console.WriteLine("Match 90:");
                    print_array(rotate_90);
                    System.Console.WriteLine("Match 180:");
                    print_array(rotate_180);
                    System.Console.WriteLine("Match 270:");
                    print_array(rotate_270);
                    //System.Console.WriteLine("Match 360:");
                    //print_array(rotate_360);
                    System.Console.WriteLine("vertical flip:");
                    print_array(flip_vertical);
                    System.Console.WriteLine("horizontal flip:");
                    print_array(flip_horizontal);
                    System.Console.WriteLine("test1: {0}.", flip_horizontal.SequenceEqual(rotate_90));
                    System.Console.WriteLine("test2: {0}.", flip_horizontal.Equals(rotate_90));
                    System.Console.WriteLine("test3: {0}.", flip_horizontal == rotate_90);
                }
                xxx++;
            }
            System.Console.WriteLine("Rules size: {0}", rules.Count);
            for (int i = 0; i < iters; i++)
            {
                int n = grid[0].Length;
                int step = 2;
                int new_dim = n * (3 / 2);
                if (n % 3 == 0)
                {
                    step = 3;
                    new_dim = n * (4 / 3);
                }
                //Create and initialize blank results 2D list.
                List<string> results = new List<string>();
                for(int j = 0; j < new_dim; j++)
                {
                    string line = "";
                    for (int k = 0; k < new_dim; k++)
                        line += " ";
                    results.Add(line);
                }
                for (int row_idx = 0; row_idx < n; row_idx += step)
                {
                    for (int col_idx = 0; col_idx < n; col_idx += step)
                    {
                        List<string> square = grab_square(grid, row_idx, col_idx, step);
                        print_array(square);
                        square = rules[square];
                        results = add_square(square, results, row_idx, col_idx, step);
                    }
                }
                grid = results;
            }
            int pt1 = 0;
            foreach (string line in grid)
                foreach (char x in line)
                    if (x == '#')
                        pt1++;
            System.Console.WriteLine("Solution to Day21 Part1: {0}", pt1);
        }
        static List<string> parse_rule(string input_string)
        {
            var rule = input_string.Split('/').ToList();
            List<string> res = new List<string>();
            foreach (var line in rule)
                res.Add(line.ToString());
            return res;
        }
        static List<string> rotate(List<string> arr)
        {

            int n = arr[0].Length;
            List<string> res = new List<string>();
            /*for (int i = 0; i < n; ++i)
            {
                string line = new string();
                for (int j = 0; j < n; ++j)
                    line.Add(' ');
                res.Add(line);
            }*/
            for (int i = 0; i < n; ++i)
            {
                string line = "";
                for (int j = 0; j < n; ++j)
                    line += arr[n - j - 1][i];
                res.Add(line);
            }
            return res;
        }
        static List<string> flip_vert(List<string> arr)
        {
            List<string> res = new List<string>();
            int n = arr[0].Length;
            for (int i = 0; i < n; i++)
            {
                res.Add(arr[n - 1 - i]);
            }
            return res;
        }
        static List<string> flip_horiz(List<string> arr)
        {
            List<string> res = new List<string>();
            int n = arr[0].Length;
            for (int i = 0; i < n; i++)
            {
                string tt = arr[i];
                tt.Reverse();
                res.Add(tt);
            }
            return res;
        }
        static List<string> grab_square(List<string> arr, int row_idx, int col_idx, int n)
        {
            List<string> res = new List<string>();
            for(int i = row_idx; i < row_idx + n; i++)
            {
                string row = arr[i];
                string new_row = row.Skip(col_idx).Take(n).ToString();
                res.Add(new_row);
            }
            return res;
        }
        static List<string> add_square(List<string> arr, List<string> result, int old_row_idx, int old_col_idx, int steps)
        {
            int dim = arr[0].Length;
            int new_row_idx = old_row_idx * (3 / 2);
            int new_col_idx = old_col_idx * (3 / 2);
            if (steps == 3)
            {
                new_row_idx = old_row_idx * (4 / 3);
                new_col_idx = old_col_idx * (4 / 3);
            }
            for (int i = 0; i < dim; i++)
                for (int j = 0; j < dim; j++)
                {
                    int x = new_row_idx + i;
                    char[] temp = result[x].ToCharArray();
                    temp[new_col_idx + j] = arr[i][j];
                    result[x] = temp.ToString();
                }
            return result;
        }
        static void print_array(List<string> arr)
        {
            foreach (string line in arr)
                System.Console.WriteLine("[{0}]", String.Join("", line));
        }
    }
}