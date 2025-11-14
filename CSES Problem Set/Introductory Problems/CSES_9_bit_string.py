"""
    Link: https://cses.fi/problemset/task/1617
"""
import sys

n = int(sys.stdin.readline())

MOD = 10**9 + 7
base = 2
ans = 1
while n:
    ans = (ans * base**(n % 2)) % MOD
    base = (base * base ) % MOD
    n //= 2
print(ans)
