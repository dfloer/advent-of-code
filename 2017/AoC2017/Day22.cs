using System;
using System.Collections.Generic;
using System.Linq;

namespace Day22
{
    partial class Program
    {
        static void Main(string[] args)
        {
            System.IO.StreamReader file = new System.IO.StreamReader(@"day22.txt");
            string raw_line;
            Dictionary<string, char> nodes = new Dictionary<string, char>();
            List<string> temp = new List<string>();
            while ((raw_line = file.ReadLine()) != null)            
                temp.Add(raw_line);
            // Create the initial "infinite" grid.
            int rows = temp.Count;
            int cols = temp[0].Length;
            for(int row_idx = -1 * (rows / 2); row_idx <= rows / 2; row_idx++)
            {
                for(int col_idx = -1 * (cols / 2); col_idx <= cols / 2; col_idx++)
                {
                    string key = row_idx + "x" + col_idx;
                    int src_row_idx = row_idx + (rows / 2);
                    int src_col_idx = col_idx + (cols / 2);
                    nodes[key] = temp[src_row_idx][src_col_idx];
                }
            }
            int new_infected = 0;
            int row_posn = 0;
            int col_posn = 0;
            int dir = 0; //0 is up, 1 is right, 2 is down, 3 is left.
            for (int step = 0; step < 10000; step++)
            {
                string node_key = row_posn + "x" + col_posn;
                char value = '.';
                try
                {
                    value = nodes[node_key];
                }
                catch (KeyNotFoundException)
                {
                    nodes[node_key] = '.';
                }
                // Step 1.
                bool infected = false;
                if (value == '#')
                    infected = true;
                if (infected)
                    dir = (dir + 1) % 4;  // rotating right is +.
                else
                    dir = (dir - 1 + 4) % 4;  // rotating left is -.
                // Step 2.
                if (infected)
                    nodes[node_key] = '.';
                else
                {
                    nodes[node_key] = '#';
                    new_infected++;
                }
                //Step 3.
                switch(dir)
                {
                    case 0:  //up
                        row_posn--;
                        break;
                    case 1:  // right
                        col_posn++;
                        break;
                    case 2:  // down
                        row_posn++;
                        break;
                    case 3:  // left
                        col_posn--;
                        break;
                }
            }
            // 4994 low. 5000 low.
            System.Console.WriteLine("Solution to Day22 Part1: {0}", new_infected);
        }
    }
}