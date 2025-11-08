"""
    Link: https://cses.fi/problemset/task/2165
"""

import sys

n = int(sys.stdin.readline())

def f(m, src, dst):
    if m == 1:
        return [(src, dst)]
    ans = []
    left =  f(m - 1, src, 6 - src - dst) # [(a1,b1), (a2,b2)]
    ans += left
    ans += [(src, dst)]
    right = f(m - 1, 6 - src - dst, dst)
    ans += right
    return ans

moves = f(n, 1, 3)
sys.stdout.write(f"{len(moves)}\n")
for a, b in moves:
    sys.stdout.write(f"{a} {b}\n")