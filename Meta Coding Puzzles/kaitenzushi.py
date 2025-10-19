# link: https://www.metacareers.com/profile/coding_puzzles?puzzle=958513514962507
from typing import List
from collections import deque
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here
  eaten = {}
  eaten_list = deque()
  length = 0
  ans = 0
  for i in range(N):
    dish = D[i]
    if dish not in eaten:
      if length == K:
        poped = eaten_list.popleft()
        del eaten[poped]
        eaten_list.append(dish)
        ans += 1
        eaten[dish] = True
      elif length < K:
        length += 1
        eaten_list.append(dish)
        ans += 1
        eaten[dish] = True
  return ans

print(getMaximumEatenDishCount(N=6,D=[1, 2, 3, 3, 2, 1],K=1))
print(getMaximumEatenDishCount(N=6,D=[1, 2, 3, 3, 2, 1],K=2))
print(getMaximumEatenDishCount(N=7,D=[1, 2, 1, 2, 1, 2, 1],K=2))
