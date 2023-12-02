import re

# Part I

with open('input.txt', 'r') as file:
    input = file.readlines()

count = 0

for line in input:
    number_list = [char for char in line if char.isdigit()]
    if len(number_list) == 1:
        number_list.append(number_list[0])

    two_digits = int(number_list[0]+number_list[-1])
    count += two_digits

print(count)

# Part II

new_count = 0

words = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0',
        }

string_numbers = []

for word in input:
    pattern = r'\d|' + '|'.join(words.keys())
    string_numbers.append(re.findall(pattern, word))

for string in string_numbers:
    numbers = [words.get(item, item) for item in string]
    numbers[:] = numbers[:1] + numbers [-1:]
    if len(numbers) == 1:
        numbers.append(numbers[0])

    new_count += int(numbers[0]+numbers[-1])

print(new_count)
