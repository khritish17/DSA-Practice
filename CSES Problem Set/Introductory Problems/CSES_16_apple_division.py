import sys 

n = int(sys.stdin.readline())
line = sys.stdin.readline().split()
weight = list(map(int, line))

ans = [float('inf')]
def f(i, grp1, grp2):
    if i == len(weight):
        ans[0] = min(ans[0], abs(grp2 - grp1))
        return
    f(i + 1, grp1 + weight[i], grp2)
    f(i + 1, grp1, grp2 + weight[i])
f(0, 0, 0)
sys.stdout.write(f"{ans[0]}")
