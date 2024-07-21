def quick_sort(arr):
    pivot_element = arr[0]
    greater_elements = []
    equal_elements = []
    lesser_elements = []

    for item in arr:
        if item < pivot_element:
            lesser_elements.append(item)
        elif item == pivot_element:
            equal_elements.append(item)
        else:
            greater_elements.append(item)
    
    return lesser_elements + equal_elements + greater_elements

import sys

read_input = sys.stdin.read
input_data = read_input().splitlines()

array_size = int(input_data[0])
array_numbers = list(map(int, input_data[1].split()))

sorted_array = quick_sort(array_numbers)
print(' '.join(map(str, sorted_array)))
