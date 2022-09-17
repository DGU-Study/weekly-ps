'''
# [BOJ_19236 청소년 상어 -Python3](https://www.acmicpc.net/problem/19236)

## 문제분석
```Python
1. 관찰
    
물고기 순서대로 찾고 이동 시키기
    - 번호가 작은 물고기 순서로 이동: 1~16 
    - 이동조건
        - 한칸씩 이동 가능
        - 다른 물고기가 있거나 빈칸으로 이동 가능
        - 상어가 있거나, 공간의 경계를 넘는 경우 이동 불가: 아닌경우만 제외하고 이동
    - 특이사항
        - 방향을 45도 반시계 회전 : 반시계 방향은 index가 증가하는 방향임을 활용

상어 이동 시키기
    - 이동조건       
        - 한 번에 여러 칸 이동 가능
        - 상어의 방향으로 이동 가능
        - 빈칸으로 이동 불가
        - 상어가 이동할 수 있는 칸이 없으면 종료
    
먹은 물고기의 값이 제일 큰 경우 탐색
    - 상어 위치에서 물고기 값 업데이트
    - 물고기 이동
    - 상어 먹을 수 있는 위치 모두 탐색 -> dfs 최대값 갱신

2. 복잡도
- dfs

3. 자료구조
- 공간: int[][]

```

## 해결코드
```Python
'''
'''
def move_fish(a,b,d):
    tmp = graph[a][b]
    stop_cnt = 0
    dr = d
    while True:
        if stop_cnt == 8: # 이동할 수 있는 칸이 없으면 이동 하지 않고 종료
            return
        na = a+dir_list[dr][0]
        nb = b+dir_list[dr][1]
        if 0<=na<4 and 0<=nb<4:
            print(a,b,x,y)
            for i in range(4):
                print(graph[i])
            print()
                
            if na==x and nb==y: # 상어가 있는 경우
                stop_cnt+=1
                if dr+1<=8:
                    dr = dr+1
                else:
                    dr = 1
            else:
                if 0<= graph[na][nb][0] <= 16:
                    graph[a][b] = graph[na][nb]
                    graph[na][nb] = tmp
                    return
        else: #공간의 경계를 넘는 경우
            stop_cnt+=1
            if dr+1<=8:
                dr = dr+1
            else:
                dr = 1
    
def move_shark(a,b,d):
    food_cnt = 0
    global ans
    max_fish = 0
    na = a+dir_list[d][0]
    nb = b+dir_list[d][1]
    print(a,b,d,max_fish)
    while True:
        if 0<=na<4 and 0<=nb<4:
            if graph[na][nb][0]==0:
                continue
            food_cnt+=1
            if max_fish < graph[na][nb][0]:
                a,b,d,max_fish = na,nb,graph[na][nb][1],graph[na][nb][0]
                
            else:
                continue
        else:
            break

    ans += max_fish
    graph[x][y][0] = 0 # 빈칸처리
    return food_cnt

import sys
si = sys.stdin.readline

# 입력부
dir_list = [(0,0),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)] # 반시계방향
graph = list()
for _ in range(4):
    row = list()
    tmp = list(map(int,si().split()))
    for i in range(4):
        row.append([tmp[2*i],tmp[2*i+1]])
    graph.append(row)

eated = [[False]*4 for _ in range(4)]
ans = 0

# 상어 처음 위치
x,y,dir = 0,0,0 # 현재 상어 위치와 방향
ans += graph[0][0][0]
graph[0][0][0] = 0 # 빈칸처리
dir = graph[0][0][1] # 방향 초기화

#while True:
# 물고기 찾기
for fish in range(1,17):
    for i in range(4):
        for j in range(4):
            if fish==graph[i][j][0]:
                # 물고기 이동
                move_fish(i,j,graph[i][j][1])
            else:
                continue

    # 상어이동 
    #if not move_shark(x,y,dir):
     #   break

#print(ans)
'''

import copy
import sys
si = sys.stdin.readline

def find_food(array, s_x, s_y):
    foods = []
    s_d = array[s_x][s_y][1]
    for i in range(1,5):
        nx = s_x+dx[s_d]*i
        ny = s_y+dy[s_d]*i
        if (0<= nx <4 and 0<=ny<4) and 1<=array[nx][ny][0]<=16:
            foods.append([nx,ny])
    return foods

def move_fish(array,s_x, s_y):
    for f in range(1,17):
        f_x,f_y=-1,-1
        for i in range(4):
            for j in range(4):
                if array[i][j][0] == f:
                    f_x,f_y=i,j
                    break
        if f_x==-1 and f_y==-1: # 물고기가 없음
            continue
        f_d = array[f_x][f_y][1]

        for i in range(8):
            nd = (f_d+i)%8
            nx, ny = f_x + dx[nd], f_y + dy[nd]
            if not (0<=nx<4 and 0<=ny<4) or (nx==s_x and ny==s_y):
                continue
            array[f_x][f_y][1]= nd
            array[f_x][f_y], array[nx][ny] = array[nx][ny], array[f_x][f_y]
            break
            


def dfs(array, s_x, s_y, socore):
    global max_socre

    # 해당 위치 물고기 먹고 최대값 갱신하기
    array[s_x][s_y][0] = -1
    socore += array[s_x][s_y][0]
    max_socre = max(max_socre, socore)

    # 물고기 이동
    move_fish(array,s_x,s_y)

    # 상어가 먹을 수 있는 위치에 대하여 모두 탐색
    food_list = find_food(array, s_x, s_y)
    for n_x,n_y in food_list:
        dfs(copy.deepcopy(array),n_x,n_y,socore)

# 입력부
array = [[] for _ in range(4)]
for i in range(4):
    tmp = list(map(int,si().split()))
    row = []
    for j in range(4):
        row.append([tmp[2*j],tmp[2*j+1]-1])
    array[i] = row

# 반시계방향
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

# dfs 탐색
max_socre = 0
dfs(array,0,0,0)
print(max_socre)
