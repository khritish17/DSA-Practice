"""
    Problem Link: https://cses.fi/problemset/task/1072
"""

n = int(input())

for k in range(1, n + 1):
    k_sq = k*k
    total_ways = (k_sq * (k_sq - 1))//2
    attacking_ways = 4 * (k - 1)*(k - 2)
    ans = total_ways - attacking_ways
    print(max(0, ans)) 