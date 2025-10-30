"""
    Problem Link: https://cses.fi/problemset/task/1068
"""
n = int(input())
seq = ""
while n != 1:
    seq += str(n) + " "
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
seq += "1"
print(seq)