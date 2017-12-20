using System;
using System.Collections.Generic;
using System.Linq;

namespace Day19
{
    partial class Program
    {
        static void Main(string[] args)
        {
            System.IO.StreamReader file = new System.IO.StreamReader(@"day19.txt");
            string raw_line;
            List<List<char>> grid = new List<List<char>>();
            while ((raw_line = file.ReadLine()) != null)
            {
                grid.Add(raw_line.ToCharArray().ToList());
            }
            // Find the starting positions, will be on first line.
            int start = 0;
            for(int i = 0; i < grid[0].Count; i++)
                if (grid[0][i] != ' ')
                    start = i;
            char dir = 'd';
            int x = 0;
            int y = start;
            int steps = 1;
            // (0, 0) is top left corner.
            List<char> letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".ToCharArray().ToList();
            List<char> result = new List<char>();
            while(true)
            {
                char val = grid[x][y];
                char next_dir = dir;
                // Only need to change direction when + found.
                if (letters.Contains(val))
                {
                    result.Add(val);
                    if (val == 'A') // A appears to be the end in the given input.
                    {
                        //steps++;
                        break;
                    }
                }
                else if (val == '+')
                {
                    next_dir = get_neighbours(grid, x, y, dir);
                }
                dir = next_dir;
                switch (dir)
                {
                    case 'd':
                        x++;
                        break;
                    case 'u':
                        x--;
                        break;
                    case 'l':
                        y--;
                        break;
                    case 'r':
                        y++;
                        break;
                }
                steps++;
            }
            string pt1 = new string(result.ToArray());
            System.Console.WriteLine("Solution to Day19 Part1: {0}", pt1);
            System.Console.WriteLine("Solution to Day19 Part2: {0}", steps);
        }
        static char get_neighbours(List<List<char>> grid, int x, int y, char dir)
        {
            char top = ' ';
            char bottom = ' ';
            char left = ' ';
            char right = ' ';
            try
            {
                top = grid[x - 1][y];
            }
            catch (ArgumentOutOfRangeException)
            { }
            try
            {
                bottom = grid[x + 1][y];
            }
            catch (ArgumentOutOfRangeException)
            { }
            try
            {
                left = grid[x][y - 1];
            }
            catch (ArgumentOutOfRangeException)
            { }
            try
            {
                right = grid[x][y + 1];
            }
            catch (ArgumentOutOfRangeException)
            { }
            char next_dir = 'x';
            if (top != ' ' && dir != 'd')
                next_dir = 'u';
            if (bottom != ' ' && dir != 'u')
                next_dir = 'd';
            if (left != ' ' && dir != 'r')
                next_dir = 'l';
            if (right != ' ' && dir != 'l')
                next_dir = 'r';
            return next_dir;
        }
    }
}