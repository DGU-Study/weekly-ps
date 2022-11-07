n, m = map(int, input().split())
s = set(list(input() for _ in range(n)))
cnt = 0

for _m in range(m):
    temp = input()
    if temp in s:
        cnt+=1

print(cnt)