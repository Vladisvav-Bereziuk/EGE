nums = []
for x in '0123456789AB':
    for y in '0123456789AB':
        res = int(f'{y}AA{x}', 12) + int(f'{x}02{y}', 14)
        if res % 80 == 0:
            nums.append(res)

print(min(nums) // 80)