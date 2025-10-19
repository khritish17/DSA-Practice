# link: https://www.metacareers.com/profile/coding_puzzles?puzzle=990060915068194
from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  cur = 1
  seconds = 0
  for target in C:
    direct = abs(target - cur)
    indirect = N - direct
    seconds += min(direct, indirect)
    cur = target
  return seconds

print(getMinCodeEntryTime(N=3, M=3, C=[1, 2, 3]))
print(getMinCodeEntryTime(N=10, M=4, C=[9, 4, 4, 8]))