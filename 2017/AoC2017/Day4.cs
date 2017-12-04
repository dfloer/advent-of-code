using System;
using System.Linq;

namespace Day4
{
    partial class Program
    {
        static void Main(string[] args)
        {
            string line;
            System.IO.StreamReader file = new System.IO.StreamReader(@"day4.txt");
            int valid_passphrases = 0;
            int i = 0;
            while ((line = file.ReadLine()) != null)
            {
                string[] split_line = line.Split();
                var results = split_line.GroupBy(x => x)
                              .Where(g => g.Count() > 1)
                              .Select(y => y.Key)
                              .ToList();                
                if (results.Count == 0)
                {
                    valid_passphrases += 1;
                }
                i++;
            }
            System.Console.WriteLine("Solution to Day4 Part1: {0}", valid_passphrases);
        }
    }
}
