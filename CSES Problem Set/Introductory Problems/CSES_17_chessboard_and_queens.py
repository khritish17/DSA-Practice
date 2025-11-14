"""
    Link: https://cses.fi/problemset/task/1624
"""

import sys
grid = []
for _ in range(8):
    line = list(sys.stdin.readline().strip("\n"))
    grid.append(line)

hash_map = {"horizontal":{},
            "vertical":{},
            "diagonal":{},
            "antidiagonal":{}}

ans = [0]
def f(i, count):
    if i == 8:
        if count == 0:
            ans[0] += 1
            return
        else:
            return
    for j in range(8):
        if grid[i][j] != "*" and i not in hash_map["horizontal"] and j not in hash_map["vertical"] and (i + j) not in hash_map["diagonal"] and (i -j) not in hash_map["antidiagonal"]:
            hash_map["horizontal"][i] = True
            hash_map["vertical"][j] = True
            hash_map["diagonal"][i + j] = True
            hash_map["antidiagonal"][i - j] = True
            f(i + 1, count - 1)
            del hash_map["horizontal"][i]
            del hash_map["vertical"][j]
            del hash_map["diagonal"][i + j]
            del hash_map["antidiagonal"][i - j]

f(0,8)
print(ans[0])
