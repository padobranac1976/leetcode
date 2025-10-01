from typing import List

def leastInterval(tasks: List[str], n: int) -> int:
    frequency_map = {}
    maximum = 0
    for t in tasks:
        if t not in frequency_map:
            frequency_map[t] = 0
        frequency_map[t] += 1
        maximum = max(maximum, frequency_map[t])
    max_freq = maximum - 1
    idle_slots = max_freq * n + max_freq
    for task, freq in frequency_map.items():
        idle_slots -= min(freq, max_freq)
        
    return max(idle_slots, 0) + len(tasks)

print(leastInterval(["A","A","A","B","B","B"], n=2))
print(leastInterval(["A","C","A","B","D","B"], n = 1))
print(leastInterval(["A","A","A", "B","B","B"], n = 3))
print(leastInterval(["A","B","A"], n = 2))