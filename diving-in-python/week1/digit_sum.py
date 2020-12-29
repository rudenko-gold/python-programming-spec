import sys

digit_string = sys.argv[1]
# digit_string = input()

answer = 0
for ch in digit_string:
    answer += ord(ch) - ord('0')

print(answer)
