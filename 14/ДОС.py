from sys import set_int_max_str_digits

set_int_max_str_digits(99999)


def convert(num):
    result = []
    while num > 0:
        result.append(num % 27)
        num = num // 27
    return result


res = 0
n = 0

x = convert(3 * (5103 ** 2020) + 3 * (729 ** 2021) - 2 * (343 ** 2022) + 27 ** 2023 - 4 * (7 ** 2024) - 2029)
for num in x:
    if num > 9:
        res += 1
print(res)
