using System;
using System.Collections.Generic;
using System.Collections;

namespace Day3
{
    partial class Program
    {
        static void Main(string[] args)
        {
            int number = 361527;
            int edge_legnth = (int)Math.Ceiling(Math.Sqrt(number));
            if(edge_legnth % 2 == 0)
            {
                edge_legnth += 1;
            }
            // What is the value in the bottom right, the maximum value for this square.
            int bottom_right = (int)Math.Pow(edge_legnth, 2);
            // How many numbers away from the bottom right corner for this square are we?
            int edge_diff = bottom_right - number;
            // The manhattan distance from the center to the bottom right corner, which will be the maximum.
            int dist_from_center = (int)Math.Sqrt(bottom_right - 1);
            // Now we find how many spots away from the bottom right corner our number is.
            // The "(edge_diff / (edge_legnth - 1))" is to account for that all the corners are the same distance away from the center and to index based on the closest corners's value.
            // The closest corner's value (ceiling corner, not floor) will be the length of the edge - 1 from the bottom right corner.
            int edge_other = edge_diff - (edge_diff / (edge_legnth - 1)) * (edge_legnth - 1);
            // Subtract this difference from the maximum possible manhattan distance.
            int pt1_res = dist_from_center - edge_other;
            System.Console.WriteLine("Day3 part1 solution: {0}", pt1_res);

            // ToDo: implement part2 programattically. I Googled for the sequence and found it online.
        }
    }
}
