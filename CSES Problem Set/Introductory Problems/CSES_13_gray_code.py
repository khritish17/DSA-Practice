"""
    Link: https://cses.fi/problemset/task/2205/
"""
import sys 

N = int(sys.stdin.readline())

n = 1
gray_code = ["0", "1"]
for _ in range(n, N):
    temp = []
    for ele in gray_code:
        temp.append("0" + ele)
    for ele in gray_code[::-1]:
        temp.append("1" + ele)
    gray_code = temp

for code in gray_code:
    print(code)

