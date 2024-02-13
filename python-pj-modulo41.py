def modular_inverse(num, modulus):
    for i in range(1, modulus):
        if (num * i) % modulus == 1:
            return i
    return None

def find_mod(num, mod):
    a = num % mod

    return a

def map_to_char(num):
    if 1 <= num <= 26:
        return chr(num + 64)  # A=1, B=2, ..., Z=26
    elif 27 <= num <= 36:
        return chr(num + 21)  # 0=27, 1=28, ..., 9=36
    elif num == 37:
        return '_'
    else:
        return None

# Given list of numbers
numbers = [104, 372, 110, 436, 262, 173, 354, 393, 351, 297, 241, 86, 262, 359, 256, 441, 124, 154, 165, 165, 219, 288, 42]

# Iterate over each number, find its modular inverse, and map to characters
result_nums = list()
result_chars = list()
for num in numbers:
    a = find_mod(num=num, mod=41)
    inverse = modular_inverse(a, 41)
    result_nums.append(inverse)
    result_char = map_to_char(inverse)
    result_chars.append(result_char)
print(result_nums)
print(result_chars)

string_result = ''
for result_char in result_chars:
    string_result = string_result + result_char
print(string_result)