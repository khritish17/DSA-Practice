"""
    Link: https://cses.fi/problemset/task/1755  
"""
import sys

line = sys.stdin.readline().rstrip("\n")
characters = list(line)
n = len(characters)
freq = {}
for letter in characters:
    if letter in freq:
        freq[letter] += 1
    else:
        freq[letter] = 1

ans = [""]*n
l, r = 0 , len(ans) - 1
if n % 2 == 0:
    # possible even pallindrome
    for letter, f in freq.items():
        if f % 2 != 0:
            print("NO SOLUTION")
            exit(0)
        else:
            count = f + 0 
            while count > 0:
                ans[l] = letter
                ans[r] = letter
                count -= 2
                l += 1
                r -= 1
else:
    # possible odd pallindrome
    odd_found = False
    odd_letter = ""
    for letter, f in freq.items():
        if f % 2 != 0 and not odd_found:
            odd_found = True
            count = f + 0
            while count > 1:
                ans[l] = letter
                ans[r] = letter
                count -= 2
                l += 1
                r -= 1
            freq[letter] = 1
            odd_letter = letter
        elif f % 2 != 0 and odd_found:
            print("NO SOLUTION")
            exit(0)
        else:
            count = f + 0 
            while count > 0:
                ans[l] = letter
                ans[r] = letter
                count -= 2
                l += 1
                r -= 1
            freq[letter] = 0
    ans[l] = odd_letter

print("".join(ans))


