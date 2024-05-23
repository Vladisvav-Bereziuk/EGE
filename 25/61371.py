from fnmatch import fnmatch

for num in range(0, 10**10, 2024):
    if fnmatch(str(num), '3?6906*4'):
        print(num)
