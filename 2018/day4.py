from datetime import datetime
from collections import defaultdict


def day4_split():
    with open('day4.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines


def parse():
    inp = day4_split()
    ds = "%Y-%m-%d %H:%M"
    res = {}
    for x in inp:
        t = datetime.strptime(x[1 : 17], ds)
        r = x[19 : ]
        res[t] = r
    return sorted(res.items())


def day4():
    p = parse()
    sleep_tracker = defaultdict(list)
    guard = 0
    for time, action in p:
        if "Guard" in action:
            a = action.split(' ')
            guard = int(a[1][1 : ])
        elif "falls asleep" in action:
            sleep_tracker[guard] += [time]
        elif "wakes up" in action:
            sleep_tracker[guard] += [time]

    # find which guard spent the most time asleep
    highest = 0
    highest_guard = 0
    for k, v in sleep_tracker.items():
        sleeping_time = 0
        for x in range(0, len(v), 2):
            sleeping_time += int((v[x + 1] - v[x]).total_seconds() // 60)
        if sleeping_time > highest:
            highest = sleeping_time
            highest_guard = k
    # For that guard, figure out which minute was most spent asleep.
    most_asleep, _ = find_most_asleep_minute(sleep_tracker[highest_guard])

    # Do the same for all guards (part 2).
    worst_minute = 0
    worst_count = 0
    worst_guard = 0
    for k, v in sleep_tracker.items():
        worst, count = find_most_asleep_minute(v)
        if count > worst_count:
            worst_count = count
            worst_minute = worst
            worst_guard = k

    return highest_guard * most_asleep, worst_guard * worst_minute


def find_most_asleep_minute(sleep_times):
    minutes = [0 for _ in range(60)]
    for x in range(0, len(sleep_times), 2):
        start, end = sleep_times[x], sleep_times[x + 1]
        for y in range(start.minute, end.minute):
            if start.hour or end.hour != 0:
                continue
            else:
                minutes[y] += 1
    return minutes.index(max(minutes)), max(minutes)


if __name__ == "__main__":
    print(f"Solution to day 3 part 1: {day4()[0]}")
    print(f"Solution to day 3 part 1: {day4()[1]}")
