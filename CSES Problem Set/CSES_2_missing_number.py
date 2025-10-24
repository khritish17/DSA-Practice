"""
    Problem Link: https://cses.fi/problemset/task/1083
"""
n = int(input())
arr = input()
arr = arr.split(" ")

full_xor = 0
obtain_xor = 0
count = 1
for ele in arr:
    obtain_xor ^= int(ele)
    full_xor ^= count
    count += 1
full_xor ^= count
print(full_xor ^ obtain_xor)