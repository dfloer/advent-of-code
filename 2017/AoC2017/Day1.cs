using System;

namespace AoC2017
{
    class Program
    {
        static void Main(string[] args)
        {
            string input_text = System.IO.File.ReadAllText(@"day1.txt");
            //var split_input = input_text.ToCharArray();
            char[] split_input = input_text.ToCharArray();
            Console.WriteLine(split_input);




            int string_length = split_input.Length;
            int running_sum = 0;
            for (int i = 0; i < string_length - 1; i++)
            {
                int a = (int)Char.GetNumericValue(split_input[i]);
                int b = (int)Char.GetNumericValue(split_input[i + 1]);

                if (a == b)
                {
                    running_sum += a;
                    Console.WriteLine("{0}: {1}, {2}", i, a, b);
                }
            }
            int first = (int)Char.GetNumericValue(split_input[0]);
            int last = (int)Char.GetNumericValue(split_input[string_length - 2]);  // Why is this -2 and not -1 for the last element?
            if (first == last)
            {
                running_sum += first;
                Console.WriteLine("first/last: {0}, {1}", first, last);
            }
            Console.WriteLine("Day1, part1 answer: {0}", running_sum);

            // Keep console window open when we end.
            Console.WriteLine("Press any key to exit.");
            System.Console.ReadKey();
        }
    }
}
