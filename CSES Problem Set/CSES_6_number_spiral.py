"""
    Problem Link: https://cses.fi/problemset/task/1071 
"""
t = int(input())
for _ in range(t):
    m, n = input().split(" ")
    m, n = int(m), int(n)

    if m >= n:
        if m % 2 != 0:
            row_val = ((m - 1)**2) + 1
            print(row_val + n - 1)
        else:
            row_val = m**2 
            print(row_val - n + 1)
    elif n > m:
        if n % 2 != 0:
            col_val = n**2
            print(col_val - m + 1)
        else:
            col_val = ((n - 1)**2)+1
            print(col_val + m - 1)