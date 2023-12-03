import re

# Input files not included in repo per copyright & Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# Replace with path to your personal input file if you would like to run the code.
input_file = 'input.txt'

# To match the format of input files for the Basilisk.
q = {3: open(input_file).read()}

num_coords = []
symbol_coords = []
for x, line in enumerate(q[3].split('\n')):
    nums = re.finditer(r'\d+', line)
    for n in nums:
        coords = []
        for i in range(len(n.group())):
            coords.append((x, n.start() + i))
        num_coords.append([int(n.group()), coords])
    symbols = re.finditer(r'[*]', line)
    for s in symbols:
        symbol_coords.append([s.group(), (x, s.start()), []])
adj_nums = []
for n in num_coords:
    for c in n[1]:
        for s in symbol_coords:
            if abs(c[0] - s[1][0]) <= 1 and abs(c[1] - s[1][1]) <= 1:
                s[2].append(n) if n not in s[2] else 0
                break
print('Day 03 Part 2:', sum([s[2][0][0] * s[2][1][0]
      for s in symbol_coords if len(s[2]) == 2]))
