'''
# [BOJ_19236 청소년 상어 -Python3](https://www.acmicpc.net/problem/19236)

## 문제분석
```Python
1. 관찰
- 

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

def sol():
    q = deque()

    



dir = [(0,0),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-11,1)] # 반시계방향
fish_table = list()
for _ in range(4):
    tmp = list(map(int,si().split()))
    row = list()
    for i in range(4):
        row.append((tmp[2*i],tmp[2*i+1]))
    fish_table.append(row)
