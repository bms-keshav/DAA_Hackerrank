import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the max_population function below.
def max_population(villages, start_cloud_positions, end_cloud_positions):
    villages = sorted(villages)
    start_cloud_positions = sorted(start_cloud_positions)
    end_cloud_positions = sorted(end_cloud_positions)

    start_idx = 0
    end_idx = 0
    active_cloud_set = set()

    cloud_pop_map = defaultdict(int)
    free_population = 0
    
    for village_idx in range(len(villages)):
        village_position = villages[village_idx][0]
        while start_idx < len(start_cloud_positions) and start_cloud_positions[start_idx][0] <= village_position:
            active_cloud_set.add(start_cloud_positions[start_idx][1])
            start_idx += 1
        while end_idx < len(end_cloud_positions) and end_cloud_positions[end_idx][0] < village_position:
            active_cloud_set.remove(end_cloud_positions[end_idx][1])
            end_idx += 1
        if len(active_cloud_set) == 1:
            villages[village_idx][2] = list(active_cloud_set)[0]
            cloud_pop_map[list(active_cloud_set)[0]] += villages[village_idx][1]
        elif len(active_cloud_set) == 0:
            free_population += villages[village_idx][1]

    return max(cloud_pop_map.values(), default=0) + free_population

def main():
    village_count = int(input().strip())
    village_populations = [int(x) for x in input().strip().split()]
    village_positions = [int(x) for x in input().strip().split()]
    villages = [[position, population, -1] for position, population in zip(village_positions, village_populations)]
    
    cloud_count = int(input().strip())
    cloud_positions = [int(x) for x in input().strip().split()]
    cloud_ranges = [int(x) for x in input().strip().split()]
    start_cloud_positions = [[cloud_positions[i] - cloud_ranges[i], i] for i in range(cloud_count)]
    end_cloud_positions = [[cloud_positions[i] + cloud_ranges[i], i] for i in range(cloud_count)]
    
    result = max_population(villages, start_cloud_positions, end_cloud_positions)
    print(result)

if __name__ == "__main__":
    main()
