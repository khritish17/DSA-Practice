"""
    Link: https://cses.fi/problemset/task/1092
"""

n = int(input())

total_sum = (n*(n + 1))//2
if total_sum % 2 == 0:
    print("YES")
    set1 = []
    set2 = []
    cur_target = total_sum // 2
    for i in range(n, 0, -1):
        if i <= cur_target:
            set1.append(str(i))
            cur_target -= i 
        else:
            set2.append(str(i))
    print(len(set1))
    print(" ".join(set1))
    print(len(set2))
    print(" ".join(set2))
else:
    print("NO")
