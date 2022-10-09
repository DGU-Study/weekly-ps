from collections import defaultdict,deque

def bfs(n,x,dic,cutting):
    d = deque()
    d.append(x)
    visited = [0]*(n+1)
    visited[x] = 1
    visited[cutting] = 1 # 끊었으니 이동하지 않도록. 
    while d:
        x = d.popleft()
        
        for value in dic[x]:
            if not visited[value]:
                visited[value] = 1
                d.append(value)
                
    return sum(visited)
    
    
def solution(n, wires):
    answer = 100+1
    
    dic = defaultdict(list)
    
    
    for lst in wires: # graph 탐색을 위한 dic정의 
        a,b = lst[0],lst[1] 
        dic[a].append(b)
        dic[b].append(a)
    
    for lst in wires:
        cut_a,cut_b = lst[0],lst[1]
        
        counter_a,counter_b = bfs(n,cut_a,dic,cut_b),bfs(n,cut_b,dic,cut_a)
        # print(counter_a,counter_b)
        answer = min( answer, abs(counter_a - counter_b))
        
        
    return answer