
from collections import deque
import sys


line = sys.stdin.readline().split()
n, m = map(int, line)

building_map = []

for _ in range(n):
    building_map.append(list(sys.stdin.readline().strip()))


def bfs(i, j):
    q = deque()
    q.append([i, j])
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
        x, y = q.popleft()
        building_map[x][y] = "#"
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < m and building_map[new_x][new_y] == ".":
                q.append([new_x, new_y])

ans = 0
for i in range(n):
    for j in range(m):
        if building_map[i][j] == ".":
            ans += 1
            bfs(i, j)
print(ans)

