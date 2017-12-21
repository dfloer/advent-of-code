using System;
using System.Collections.Generic;
using System.Linq;

namespace Day20
{
    partial class Program
    {
        static void Main(string[] args)
        {
            System.IO.StreamReader file = new System.IO.StreamReader(@"day20.txt");
            string raw_line;
            Dictionary<int, List<long>> particles = new Dictionary<int, List<long>>();
            int i = 0;
            while ((raw_line = file.ReadLine()) != null)
            {
                List<string> test = raw_line.Split(new string[] {"=", ", ", ",", "<", ">"}, StringSplitOptions.None).ToList();
                string[] e = { test[2], test[3], test[4], test[8], test[9], test[10], test[14], test[15], test[16] };
                List<long> particle_info = e.Select(long.Parse).ToList();
                particles[i] = particle_info;
                i++;
            }
            var particles_copy = particles.ToDictionary(e => e.Key, e => e.Value);
            i = 0;
            List<int> closest = new List<int>(10000);
            // 10,000 chosen because it was more than enough (tested out to 1,000,000).
            while(i <= 10000)
            {
                particles = update_position(particles);
                closest.Add(find_closest(particles));
                i++;
            }
            System.Console.WriteLine("Solution to Day20 Part1: {0}", closest.Last());
            i = 0;
            while (i <= 1000)
            {
                particles_copy = update_position(particles_copy);
                particles_copy = collide(particles_copy);
                i++;
            }
            System.Console.WriteLine("Solution to Day20 Part2: {0}", particles_copy.Count);
        }
        static Dictionary<int, List<long>> update_position(Dictionary<int, List<long>> particles)
        {
            foreach(int key in Enumerable.Range(0,1000))
            {
                List<long> p = new List<long>();
                try
                {
                    p = particles[key];
                }
                catch
                {
                    continue;
                }
                long x = p[0];
                long y = p[1];
                long z = p[2];
                long x_v = p[3];
                long y_v = p[4];
                long z_v = p[5];
                long x_a = p[6];
                long y_a = p[7];
                long z_a = p[8];

                x_v += x_a;
                y_v += y_a;
                z_v += z_a;

                x += x_v;
                y += y_v;
                z += z_v;

                long[] new_part = { x, y, z, x_v, y_v, z_v, x_a, y_a, z_a };
                particles[key] = new_part.ToList();
            }
            return particles;
        }
        static int find_closest(Dictionary<int, List<long>> particles)
        {
            long closest_val = 9223372036854775807;
            int closest_idx = -1;
            foreach (int key in Enumerable.Range(0, 1000))
            {
                List<long> p = new List<long>();
                try
                {
                    p = particles[key];
                }
                catch (KeyNotFoundException)
                {
                    continue;
                }
                long x = p[0];
                long y = p[1];
                long z = p[2];
                long manhattan = Math.Abs(0 - x) + Math.Abs(0 - y) + Math.Abs(0 - z);
                if (manhattan < closest_val)
                {
                    closest_val = manhattan;
                    closest_idx = key;
                }
            }
            return closest_idx;
        }
        static Dictionary<int, List<long>> collide(Dictionary<int, List<long>> particles)
        {
            HashSet<int> dupes = new HashSet<int>();
            foreach (var p in particles)
            {
                // I couldn't get this working with either finding duplicates via a Dictionary or using Linq to find dupes.
                var val = p.Value.Take(3).ToList();
                var key = p.Key;
                foreach (var pp in particles)
                {
                    var val_2 = pp.Value.Take(3).ToList();
                    var key_2 = pp.Key;
                    if (val.SequenceEqual(val_2) && !(key == key_2))
                    {
                        dupes.Add(key);
                        dupes.Add(key_2);
                    }
                }
            }
            foreach (int k in dupes)
                particles.Remove(k);
            return particles;
        }
    }
}