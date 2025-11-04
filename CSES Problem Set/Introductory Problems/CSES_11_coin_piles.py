"""
    Link: https://cses.fi/problemset/task/1754
"""
import sys

def is_int(n):
    rem = n - (n * 10)//10
    if rem == 0:
        return True
    return False

t = int(sys.stdin.readline())
for _ in range(t):
    line = sys.stdin.readline().split()
    a, b = map(int, line)
    x = (2*a - b)/3
    y = (2*b - a)/3
    if x >= 0 and y >=0 and is_int(x) and is_int(y):
        print("YES")
    else:
        print("NO")