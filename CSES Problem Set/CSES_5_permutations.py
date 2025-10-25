"""
    Problem Link: https://cses.fi/problemset/task/1070
"""

n = int(input())
if n == 1:
    print("1")
    exit()

elif 2 <= n <= 3:
    print("NO SOLUTION")
    exit()
even = []
odd = []

for i in range(1, n + 1):
    if i % 2 == 0:
        even.append(str(i))
    else:
        odd.append(str(i))
ans = " ".join(even + odd)
print(ans)