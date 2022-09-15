'''
# [BOJ_16236 아기 상어 -Python3](https://www.acmicpc.net/problem/16236)

## 문제분석
```Python
1. 관찰
> -

2. 복잡도
-

3. 자료구조
-

```

## 해결코드
```Python
'''
from collections import deque
import sys
si = sys.stdin.readline

n = int(si()) # 공간의 크기
matrix = list() # 공간
q = deque([])

for i in range(n):
    row = list(map(int,si().split())) 
    matrix.append(row)
    for j in range(n):
        if row[j]==9:
            q.append((i,j))

dx, dy = [-1,1,0,0], [0,0,-1,1]
ans = 0
shark = 2 # 아기 상어의 크기 2로 시작

while q:
    y,x = q.popleft()
    for i in range(4):
        ny,nx = dy[i]+y, dx[i]+x
        if 0<=ny<n and 0<=nx<n and 0<matrix[ny][nx]<9:
            

            if 0 < matrix[ny][nx] < shark:
                matrix[ny][nx] = 0
                q.append((ny,nx))
            elif matrix[ny][nx] == 0 or matrix[ny][nx] == shark:
                q.append((ny,nx))

print(ans)