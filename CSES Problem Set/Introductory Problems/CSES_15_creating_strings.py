import sys

string = sys.stdin.readline().strip("\n")

freq = {}
for ele in "abcdefghijklmnopqrstuvwxyz":
    freq[ele] = 0
for ele in string:
    if ele in freq:
        freq[ele] += 1

ans = []
def f(prev):
    if len(prev) == len(string):
        ans.append(prev)
        return
    for char, fr in freq.items():
        if fr > 0:
            freq[char] -= 1
            f(prev + char)
            freq[char] += 1

f("")
sys.stdout.write(f"{len(ans)}\n")
for new_str in ans:
    sys.stdout.write(f"{new_str}\n")