def unlimited_knapsack(case_count, test_cases):
    final_results = []
    
    for test_case in test_cases:
        (item_count, max_sum) = test_case[0]
        item_values = test_case[1]
        
        # Initialize dp array
        dp_array = [0] * (max_sum + 1)

        for value in item_values:
            for current_value in range(value, max_sum + 1):
                dp_array[current_value] = max(dp_array[current_value], dp_array[current_value - value] + value)
        
        final_results.append(dp_array[max_sum])
    
    return final_results

import sys

read_input = sys.stdin.read
input_data = read_input().splitlines()

case_count = int(input_data[0])
test_cases = []

current_line = 1
for _ in range(case_count):
    item_count, max_sum = map(int, input_data[current_line].split())
    item_values = list(map(int, input_data[current_line + 1].split()))
    test_cases.append(((item_count, max_sum), item_values))
    current_line += 2

final_results = unlimited_knapsack(case_count, test_cases)

for result in final_results:
    print(result)
