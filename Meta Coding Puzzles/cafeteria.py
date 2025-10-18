# Link : https://www.metacareers.com/profile/coding_puzzles?puzzle=203188678289677
from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  # left boundary
  S.sort()
  ans = 0
  g = S[0] - 1
  ans += g // (K + 1)
  for i in range(1, M):
    g = S[i] - S[i - 1] - 1
    ans += (g - K)//(K + 1)
  g = N - S[-1]
  ans += g //(K + 1)
  return ans
