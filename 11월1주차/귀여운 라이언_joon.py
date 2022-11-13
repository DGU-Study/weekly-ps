from collections import deque

n, k = map(int,input().split())
info = list(map(int,input().split())) 

ans = float('INF')

cnt,left,right = 0,0,0

if info[left] == 1:
  cnt += 1

while left < len(info) and right < len(info):
  #라이언 < k , right 포인터 옮기기
  if cnt < k:
    right += 1
    if right < len(info) and info[right] == 1:
      cnt += 1
    #라이언 >= k , left 포인터 옮겨서 개수 최소화
  else :
    if cnt == k:
      ans = min(ans, right - left +1)
    if left < len(info) and info[left] == 1:
      cnt -= 1
    left += 1
if ans == float('INF'):
  print(-1)
else:
  print(ans)