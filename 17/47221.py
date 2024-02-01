nums = list(map(int, open('47221.txt').readlines()))
max_num = -100000
max_square = 0
count = 0

for num in nums:
    if abs(num) % 10 == 3:
        max_num = max(max_num, num)

for i in range(len(nums) - 1):
    # xor можно заменить !=
    if ((abs(nums[i]) % 10 == 3) != (abs(nums[i + 1]) % 10 == 3)) and (nums[i + 1]**2 + nums[i]**2 >= max_num**2):
        count += 1
        max_square = max(max_square, nums[i + 1]**2 + nums[i]**2)
print(count, max_square)