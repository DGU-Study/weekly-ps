def search_base_camp(i,j):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    from collections import deque

    d= deque()
    d.append([0,i,j])
    visited =  [[0]*n for _ in range(n)]
    visited[i][j] = 1
    answer_list = []
    flag = 20
    while d:
        cnt,x,y = d.popleft()

        if arr[x][y] == 1:
            if flag == 20:
                answer_list.append([x,y])
                flag = cnt
            elif flag == cnt:
                answer_list.append([x,y])
            else:
                continue
        
        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if 0<=a<n and 0<=b<n and not visited[a][b] and arr[a][b] != 2:
                visited[a][b] = 1
                d.append([cnt+1,a,b])
    answer_list = sorted(answer_list,key=lambda x: (x[0],x[1]))
    
    return answer_list[0][0],answer_list[0][1]

        
def move():
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    from copy import deepcopy
    from collections import deque
    d = deque()

    for idx,l in enumerate(store):

        visited = [[0]*n for _ in range(n)]
        d.append([idx,idx+1,l[0],l[1],visited,False]) # False : 아직 베이스 캠프에 안갔다는 뜻 

    answer_cnt = 0
    while d:
        index,cnt,x,y,vis,flag = d.popleft()
    
        if answer[index] == 1:
            continue
    
        if not flag:
            a,b = search_base_camp(x,y)
            visited[a][b] = 1
            arr[a][b] = 2
            d.append([index,cnt,a,b,visited,True]) # 베이스 캠프에 들렸다는 뜻 
        else:
            if [x,y] == [store[index][0],store[index][1]]:
                answer_cnt  = max(answer_cnt,cnt)
                answer[index] = 1
                arr[x][y] = 2
                if sum(answer) == m:
                    print(answer_cnt)
                    break
            for i in range(4):
                a,b = x+dx[i],y+dy[i]
                
                if 0<=a<n and 0<=b<n and not vis[a][b] and arr[a][b] == 0:
                    copy_vis = deepcopy(vis) 
                    copy_vis[a][b] = 1

                    d.append([index,cnt+1,a,b,copy_vis,flag])
                


import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
answer = [0]*m
store =  []
for _ in range(m):
    a,b  = map(int,input().split())
    a,b = a-1,b-1

    store.append([a,b])

move()


