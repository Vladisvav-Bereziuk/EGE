parts = open('39253.txt').read().split('D')

max_len = 0
for i in range(len(parts) - 1):
    # Не забываем про букву D, поэтому +1
    max_len = max(max_len, len(parts[i]) + len(parts[i + 1]) + 1)
print(max_len)

# D1111111D111111D1111D1D11111111D111111D
# 1111111 111111 1111 1 11111111 111111