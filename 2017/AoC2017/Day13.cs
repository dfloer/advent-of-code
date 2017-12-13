using System;
using System.Collections.Generic;
using System.Linq;

namespace Day13
{
    partial class Program
    {
        static void Main(string[] args)
        {
            System.IO.StreamReader file = new System.IO.StreamReader(@"day13.txt");
            string raw_line;
            Dictionary<int, int> firewall_ranges = new Dictionary<int, int>();
            while ((raw_line = file.ReadLine()) != null)
            {
                List<string> line = raw_line.Split(new string[] {": " }, StringSplitOptions.None).ToList();
                firewall_ranges[int.Parse(line[0])] = int.Parse(line[1]);
            }
            List<int> steps = new List<int>();
            foreach(KeyValuePair<int, int> entry in firewall_ranges)
            {
                int picosecond = entry.Key;
                int res = update_scanner_posn(firewall_ranges[picosecond], picosecond);
                // We're only in the same spot as the scanner if res is 0, otherwise we escaped it.
                if (res == 0)
                    steps.Add(firewall_ranges[picosecond] * picosecond);
            }
            int pt1 = steps.Sum();
            System.Console.WriteLine("Solution to Day12 Part1: {0}", pt1);
            //System.Console.WriteLine("Solution to Day12 Part2: {0}", pt2);
        }
        static int update_scanner_posn(int range, int picosecond)
        {
            // This is where a scanner should be, assuming it started at 0 at t=0.
            int offset = picosecond % ((range - 1) * 2);
            // Handle coming back up from the bottom.
            if (offset > range - 1)
                return 2 * (range - 1) - offset;
            else
                return offset;
        }
    }
}
