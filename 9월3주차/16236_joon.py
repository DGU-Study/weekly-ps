#16236 아기 상어
from collections import deque 
INF = 1e9

n = int(input()) #공간의 크기
graph = [list(map(int,input().split())) for _ in range(n)] #모든 칸에 대한 정보 입력 

dx = [-1,1,0,0]
dy = [0,0,-1,1]

#초기 크기와 위치
inst_size = 2 
inst_x, inst_y = 0,0

for i in range(n):
  for j in range(n):
    if graph[i][j] == 9:
      graph[i][j] = 0 # 그 위치엔 아무것도 없다고 생각
      inst_x, inst_y = i,j 

#최단 거리만을 계산하는 bfs함수
def bfs():
  #초기화 : -1이면 도달할 수 없음
  dist = [[-1] * n for _ in range(n)]
  queue = deque([(inst_x, inst_y)])
  dist[inst_x][inst_y] = 0 # 처음 위치는 도달 가능
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx and nx < n and 0 <= ny and ny < n:
        # 자기보다 작거나 같은 경우에 지나갈 수 있다
        if dist[nx][ny] == -1 and graph[nx][ny] <= inst_size:
          dist[nx][ny] = dist[x][y] + 1 
          queue.append((nx,ny))
  return dist


#최단 거리 테이블이 주어졌을 때, 먹을 물고기를 찾는 함수 
def hunt(dist):
  x,y = 0,0 
  min_dist = INF
  for i in range(n):
    for j in range(n):
      #도달이 가능하고 먹을 수 있는 물고기임 
      if dist[i][j] != -1 and 1 <= graph[i][j] and graph[i][j] < inst_size:
        #가장 가까운 한마리만 선택 
        if dist[i][j] < min_dist:
          x,y = i,j
          min_dist = dist[i][j]
  
  if min_dist == INF: #먹을 수 있는 물고기 없음
    return None
  else:
    return x,y, min_dist 
result = 0 # 최종 답
ate = 0 #현재 먹은 양 

while True:
  #먹을 수 있는 물고기의 위치 찾기
  value = hunt(bfs())
  #먹을 수 있는 물고기 없는 경우, 현재까지 움직인 거리 출력
  if value == None:
    print(result)
    break
  else: #현재 위치 갱신 및 이동 거리 변경 
    inst_x, inst_y = value[0], value[1]
    result += value[2]

    #먹은 위치엔 0으로 처리
    graph[inst_x][inst_y] = 0
    ate += 1 

    #자신의 현재 크기 이상으로 먹은 경우, 크기 증가
    if ate >= inst_size:
      inst_size += 1 
      ate = 0