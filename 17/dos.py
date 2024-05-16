count = 0
max_pair = 0
max_num = 0
nums = list(map(int, open('dos.txt').readlines()))
for num in nums:
    if num % 19 == 0:
        max_num = max(max_num, num)

for i in range(len(nums) - 1):
    if nums[i] > max_num or nums[i+1] > max_num:
        count += 1
        print(count)
        max_pair = max(nums[i]+nums[i+1],max_pair)
        print(max_pair)

