"""
    Problem Link: https://cses.fi/problemset/task/1069
"""
dna = input()
cur_ele = ""
count = 0
max_count = 1
for ele in dna:
    if ele == cur_ele:
        count += 1
        max_count = max(max_count, count)
    else:
        max_count = max(max_count, count)
        count = 1
        cur_ele = ele
print(max_count)