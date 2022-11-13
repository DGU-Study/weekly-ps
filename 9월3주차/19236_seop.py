
def get_nextxy(i,j,x): # 방향에 대한 다음 x y 좌표 반환 
    dx = [0,-1,-1,0,1,1,1,0,-1]
    dy = [0,0,-1,-1,-1,0,1,1,1]

    return i+dx[x],j+dy[x]


def fish_rotate(array,sx,sy): # 물고기 돌리는 함수 
    dic  = {} 
    for i in range(4):
        for j in range(4):
            if array[i][j]:
                
                f,fd = array[i][j][0],array[i][j][1]
      
                dic[f] = [i,j,fd]

    for fish in sorted(dic.keys()):

        x,y,dir = dic[fish][0],dic[fish][1],dic[fish][2]

        while 1:
            
            next_x,next_y = get_nextxy(x,y,dir)


            if (0<=next_x<4 and 0<=next_y<4) and [next_x,next_y]!=[sx,sy]:

                if array[next_x][next_y] ==0:
                    array[next_x][next_y] = [fish,dir]
                    array[x][y] = 0
                    dic[fish] = [next_x,next_y,dir]
      
                    break
                else:
                        
                    change_fish = array[next_x][next_y][0]
                    array[x][y] = [array[next_x][next_y][0],array[next_x][next_y][1]]
                    array[next_x][next_y] = [fish,dir]

                    dic[fish] = [next_x,next_y,dir]
                    dic[change_fish] = [x,y,dic[change_fish][2]]


                    

                    break
            else:
                if dir == 8:
                    dir = 1
                else:
                    dir = dir +1 

    return array


from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline

arr = [[0]*4 for _ in range(4)]

for idx, _ in enumerate(range(4)):
    a1,a2,b1,b2,c1,c2,d1,d2 = map(int,input().split())
    arr[idx][0] = [a1,a2]
    arr[idx][1] = [b1,b2]
    arr[idx][2] = [c1,c2]
    arr[idx][3] = [d1,d2]



sx,sy = 0,0
weight,shark_d = arr[0][0][0],arr[0][0][1]
arr[0][0] = 0

d = deque()
d.append([sx,sy,shark_d,weight,arr])



def bfs():
    answer = 0

    while d:



        sx,sy,sd,weight,curr_arr = d.popleft()
        curr_arr[sx][sy] = 0

        answer = max(answer,weight)

 
                
        new_arr = fish_rotate(deepcopy(curr_arr),sx,sy)
        
    
        
        can_eat_fish = []

        temp_sx,temp_sy = sx,sy
        while 1:
            next_sx,next_sy = get_nextxy(temp_sx,temp_sy,sd)
            
            if 0<=next_sx<4 and 0<=next_sy<4:
                if new_arr[next_sx][next_sy]:
                    f,fd = new_arr[next_sx][next_sy]
                    can_eat_fish.append([f,fd,next_sx,next_sy])


                temp_sx,temp_sy = next_sx,next_sy

            else:
                break
        
        for move_to_fish,next_dir,next_sx,next_sy in can_eat_fish:

            d.append([next_sx,next_sy,next_dir,weight+move_to_fish,deepcopy(new_arr)])


    return answer

            


a = bfs()


print(a)

    




