def build_string(text):
    unique_chars = set(text)
    return len(unique_chars)

import sys

read_input = sys.stdin.read
input_data = read_input().splitlines()

string_count = int(input_data[0])
outputs = []
for idx in range(1, string_count + 1):
    current_text = input_data[idx]
    output = build_string(current_text)
    outputs.append(output)

for output in outputs:
    print(output)
