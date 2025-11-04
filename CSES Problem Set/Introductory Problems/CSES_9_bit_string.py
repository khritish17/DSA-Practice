"""
    Link: https://cses.fi/problemset/task/1617
"""
import sys

n = int(sys.stdin.readline())

MOD = 10**9 + 7
base = 2
expo = n
ans = 1

while expo:
    if expo % 2 == 1: # equivalent to check the last set bit
        ans = (ans * base) % MOD
    base = (base * base) % MOD
    expo //= 2
print(ans) 


