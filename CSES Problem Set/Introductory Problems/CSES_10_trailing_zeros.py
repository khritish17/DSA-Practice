"""
    Link: https://cses.fi/problemset/task/1618
"""
import sys 

n = int(sys.stdin.readline())
ans = 0
while n > 0:
    n //= 5
    ans += n
print(ans)