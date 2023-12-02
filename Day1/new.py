# import re

# DIGIT_STRINGS = {
#     'zero': 0,
#     'one': 1,
#     'two': 2,
#     'three': 3,
#     'four': 4,
#     'five': 5,
#     'six': 6,
#     'seven': 7,
#     'eight': 8,
#     'nine': 9,
# }
# regex = r'\d|'+r"|".join(DIGIT_STRINGS)
# regex_reverse = r'\d|'+r"|".join(d[::-1] for d in DIGIT_STRINGS)


# def get_value(line: str) -> int:
#     first_digit = re.search(regex, line)[0]
#     last_digit = re.search(regex_reverse, line[::-1])[0][::-1]
#     return int(f"{DIGIT_STRINGS.get(first_digit, first_digit)}{DIGIT_STRINGS.get(last_digit, last_digit)}")



# if __name__ ==  "__main__":

#     ans = 0

#     with open("input.txt", "r") as f:
#         for line in f:
#             ans += get_value(line.strip())
    
#     print(ans)

import re

mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

sum_ = 0

with open("input.txt", "r") as f:
    for line in f:
        digits = re.findall(f"(?=(\d|{'|'.join(mapping.keys())}))", line)
        first_digit = mapping[digits[0]] if len(digits[0]) > 1 else digits[0]
        last_digit = mapping[digits[-1]] if len(digits[-1]) > 1 else digits[-1]
        sum_ += int(first_digit + last_digit)

print(sum_)