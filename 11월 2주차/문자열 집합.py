#문자열 집합 
n,m = map(int,input().split())
letters = list(input() for _ in range(n))
check = list(input() for _ in range(m))

cnt = 0
for i in check:
  if i in letters:
    cnt += 1
print(cnt)