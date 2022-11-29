import sys

n, m = map(int, sys.stdin.readline().split())
strings = [sys.stdin.readline().strip() for _ in range(n)]
cnt = 0

for _ in range(m):
    temp = sys.stdin.readline().strip()
    for s in strings:
        if temp == s[:len(temp)]:
            cnt += 1
            break
print(cnt)