"""
    Problem Link: https://cses.fi/problemset/task/1094
"""
n = int(input())
arr = input().split(" ")
cur_ele = int(arr[0])

moves = 0
for ele in arr:
    if int(ele) < cur_ele:
        moves += abs(int(ele) - cur_ele)
    else:
        cur_ele = int(ele)
print(moves)