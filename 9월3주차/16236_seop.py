def search_feed(sx,sy,level):
    
    feed_list = []

    visited = [[0]*N for _ in range(N)]

    d_feed = deque()
    d_feed.append([sx,sy,0])

    while d_feed:
        x,y,cnt = d_feed.popleft()
        
        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if 0<=a<N and 0<=b<N and not visited[a][b] and arr[a][b]<=level:
                if 0<arr[a][b]<level:
                    visited[a][b] = 1
                    feed_list.append([a,b,cnt+1])
                
                
                else: 
                    visited[a][b] = 1
                    d_feed.append([a,b,cnt+1])


    feed_list = sorted(feed_list,key=lambda x: (-x[2],-x[0],-x[1]))

    if feed_list:
        x,y,dis= feed_list.pop()
        return x,y,dis
                    
    
    return 0,0,0


from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(N):
    for j in range(N):

        if arr[i][j] == 9:
            sx,sy = i,j
            arr[i][j] = 0

def bfs(sx,sy):
    
    feed = 0
    level = 2
    answer = 0

    while 1:
    
        fx,fy,distance = search_feed(sx,sy,level)
        # print('dff',distance,fx,fy)
        if distance == 0:
            break

        else:
            arr[fx][fy] = 0
            sx,sy = fx,fy
            feed += 1 
            if feed == level :
                level +=1 
                feed = 0

            answer += distance
    return answer 

  

a = bfs(sx,sy)
print(a)