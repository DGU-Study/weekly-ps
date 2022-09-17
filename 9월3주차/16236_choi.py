'''
# [BOJ_16236 아기 상어 -Python3](https://www.acmicpc.net/problem/16236)

## 문제분석
```Python
1. 관찰
- 먹을 수 있는 물고기 찾기
- 다중 조건 정렬 ->  key = lambda x: (x[0], x[1], x[2])

- 가장 가까운 물고기 먹기 반복

2. 복잡도
- O(n*n*n)

3. 자료구조
- 공간: int[][]
- 상어 위치: deque
- 거리, 방문처리: int[][]
- 가까운 물고기 위치: int[]

```

## 해결코드
```Python
'''
from collections import deque
import sys
si = sys.stdin.readline

n = int(si()) # 공간의 크기
matrix = list() # 공간

x,y,size = 0,0,2

for i in range(n):
    row = list(map(int,si().split())) 
    matrix.append(row)
    for j in range(n):
        if row[j]==9:
            x=i
            y=j

dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0
ans = 0

def find_fish(x,y,shark_size):
    distance = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    
    q = deque()
    q.append((x,y))
    visited[x][y]=1
    tmp = []
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=ny<n and 0<=nx<n and visited[nx][ny]==0:
                if matrix[nx][ny] <= shark_size:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                    if matrix[nx][ny] < shark_size and matrix[nx][ny] != 0:
                        tmp.append((nx,ny,distance[nx][ny]))
    return sorted(tmp,key=lambda x: (-x[2],-x[0],-x[1]))

# 가까운 물고기 먹을 수 있을 때까지 먹기
while True:
    shark = find_fish(x,y,size)

    if len(shark)==0:
        break

    nx,ny,dist = shark.pop()

    ans += dist
    matrix[x][y],matrix[nx][ny] = 0,0

    x,y=nx,ny
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0

print(ans)