# Link: https://www.metacareers.com/profile/coding_puzzles?puzzle=870874083549040
def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  c = list(C)
  p_left = [0] * N
  p_right = [0] * N
  b_left = [0] * N
  b_right = [0] * N
  for i in range(N):
    ele_left = c[i]
    if ele_left == "P":
      p_left[i] = 1 + (p_left[i - 1] if i - 1 >= 0 else 0)
      b_left[i] = b_left[i - 1] if i - 1 >= 0 else 0
    elif ele_left == "B":
      b_left[i] = 1 + (b_left[i - 1] if i - 1 >= 0 else 0)
      p_left[i] = p_left[i - 1] if i - 1 >= 0 else 0
    else:
      p_left[i] = p_left[i - 1] if i - 1 >= 0 else 0
      b_left[i] = b_left[i - 1] if i - 1 >= 0 else 0
      
      
    j = N - i - 1
    ele_right = c[j]
    if ele_right == "P":
      p_right[j] = 1 + (p_right[j + 1] if j + 1 < N else 0)
      b_right[j] = b_right[j + 1] if j + 1 < N else 0
    elif ele_right == "B":
      b_right[j] = 1 + (b_right[j + 1] if j + 1 < N else 0)
      p_right[j] = p_right[j + 1] if j + 1 < N else 0
    else:
      b_right[j] = b_right[j + 1] if j + 1 < N else 0
      p_right[j] = p_right[j + 1] if j + 1 < N else 0

  ans = 0
  for i in range(N):
    ele = c[i]
    if ele == "A":
      # PAB
      p_left_count = (p_left[i - X] if i - X >= 0 else 0) - (p_left[i - Y - 1] if i - Y - 1>= 0 else 0)
      b_right_count =  (b_right[i + X] if i + X < N else 0) - (b_right[i + Y + 1] if i + Y + 1< N else 0)
      ans += p_left_count * b_right_count
      
      # BAP
      b_left_count = (b_left[i - X] if i - X >= 0 else 0) - (b_left[i - Y - 1] if i - Y - 1 >= 0 else 0)
      p_right_count = (p_right[i + X] if i + X < N else 0) - (p_right[i + Y + 1] if i + Y + 1 < N else 0)
      ans += p_right_count * b_left_count
  return ans