using System;

namespace AoC2017
{
    class Program
    {
        static void Main(string[] args)
        {
            string input_text = System.IO.File.ReadAllText(@"day1.txt");
            char[] split_input = input_text.ToCharArray();

            int string_length = split_input.Length;
            int pt1_running_sum = 0;
            for (int i = 0; i < string_length - 1; i++)
            {
                int a = (int)Char.GetNumericValue(split_input[i]);
                int b = (int)Char.GetNumericValue(split_input[i + 1]);

                if (a == b)
                {
                    pt1_running_sum += a;
                }
            }
            int first = (int)Char.GetNumericValue(split_input[0]);
            int last = (int)Char.GetNumericValue(split_input[string_length - 2]);  // Why is this -2 and not -1 for the last element?
            if (first == last)
            {
                pt1_running_sum += first;
            }

            Console.WriteLine("Day1, part1 answer: {0}", pt1_running_sum);
            int pt2_running_sum = 0;
            for (int i = 0; i < string_length; i++)
            {
                int a = (int)Char.GetNumericValue(split_input[i]);
                int halfway = (i + (string_length / 2)) % string_length;
                int b = (int)Char.GetNumericValue(split_input[halfway]);

                if (a == b)
                {
                    pt2_running_sum += a;
                }
            }

            Console.WriteLine("Day1, part2 answer: {0}", pt2_running_sum);

            // Keep console window open when we end.
            Console.WriteLine("Press any key to exit.");
            System.Console.ReadKey();
        }
    }
}
