from collections import deque

def solution(n, wires):
    def bfs(x,y):
        visited = [0 for _ in range(n+1)]
        visited[x] = 1 
        queue = deque([x])
        cnt = 0 
        
        # 송전탑 완전 탐색
        while queue: 
            v = queue.popleft()
            cnt += 1 
            for a in graph[v]:
                if not visited[a] and a != y: 
                    visited[a] = 1
                    queue.append(a)
        return cnt 
    
    graph = [[] for _ in range(n+1)]
    for x,y in wires: #양방향 그래프 연결 정보 저장 
        graph[x].append(y)
        graph[y].append(x)
        
    answer = float('INF')
    for x,y in wires:
        answer = min(abs(n - bfs(x,y) - bfs(x,y)), answer)  #기존 answer와 현재 해당하는 와이어 끊었을 때 노드 차이 비교
    return answer