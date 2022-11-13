#접두사 찾기 
n,m = map(int,input().split())
letters = list(input() for _ in range(n))
check = list(input() for _ in range(m))

cnt = 0
for i in range(m):
  for j in range(n):
    if letters[j].startswith(check[i]):
      cnt += 1
      break 
print(cnt)