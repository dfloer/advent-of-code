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
            int pt1_valid_passphrases = 0;
            int pt2_valid_passphrases = 0;
            while ((line = file.ReadLine()) != null)
            {
                string[] split_line = line.Split();
                var results = split_line.GroupBy(x => x)
                              .Where(g => g.Count() > 1)
                              .Select(y => y.Key)
                              .ToList();                
                if (results.Count == 0)
                {
                    pt1_valid_passphrases += 1;
                    if (IsAnagram(split_line) == false)
                    {
                        pt2_valid_passphrases += 1;
                    }
                }
            }
            System.Console.WriteLine("Solution to Day4 Part1: {0}", pt1_valid_passphrases);
            System.Console.WriteLine("Solution to Day4 Part1: {0}", pt2_valid_passphrases);
        }

        static bool IsAnagram(string[] line_string)
        {
            for(int i = 0; i < line_string.Length; i++)
            {
                for(int j = i + 1; j < line_string.Length; j++)
                {
                    char[] a = line_string[i].ToCharArray();
                    char[] b = line_string[j].ToCharArray();
                    Array.Sort(a);
                    Array.Sort(b);
                    // Not sure exactly why a == b doesn't work here, but this does work correctly.
                    if (a.SequenceEqual(b))
                    {
                        return true;
                    }
                }
            }
            return false;
        }
    }
}
