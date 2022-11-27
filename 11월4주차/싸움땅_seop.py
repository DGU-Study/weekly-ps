def next_xy(d,x,y): #방향에 대해서 다음으로 이동하는 칸의 좌표를 반환
    if d == 0:
        return x-1,y
    elif d == 1:
        return x,y+1
    elif d == 2:
        return x+1,y
    return x,y-1

def loser_move(player,d,x,y):
    # print('loser',player,d,x,y)
    def next_direction(d): # 현재 방향에서 오른쪽으로 90도 회전할 때
        if d<3:
            return d+1
        return 0

    if gun[player]:
        arr[x][y].append(gun[player])# 진사람은 현재 위치에 총을 버려야함 
        arr[x][y] = sorted(arr[x][y]) 
        gun[player] = 0
    
    while 1:
        a,b = next_xy(d,x,y)

        if 0<=a<n and 0<=b<n and not curr_location[a][b]:
            
            curr_location[a][b] = player
            curr_direction[player] = d

            # print(player,a,b,curr_location)
            player_location[player] = [a,b]
            if arr[a][b]:
                gun[player] = arr[a][b].pop()
            break
        else:
            d = next_direction(d)
            
def winner_move(player,x,y):
    if arr[x][y]:
        if gun[player]<arr[x][y][-1]:
            arr[x][y].append(gun[player])# 진사람은 현재 위치에 총을 버려야함 
            arr[x][y] = sorted(arr[x][y]) 
            gun[player] = arr[x][y].pop()



def reverse_direction(d): # 현재 방향에서 정반대로 회전할 때
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    return 1


def fight(player1,player2,answer):

    player1_force = base_force[player1] + gun[player1]
    player2_force = base_force[player2] + gun[player2]
    # print('fight',player1,player2,player1_force,player2_force)
    if player1_force>player2_force:
        answer[player1]+=abs(player1_force-player2_force)
        return player1,player2,answer # winner,loser
    elif player1_force<player2_force:
        answer[player2]+=abs(player1_force-player2_force)
        return player2,player1,answer
    else:
        if base_force[player1]>base_force[player2]:
            answer[player1]+=abs(player1_force-player2_force)
            return player1,player2,answer
        else:
            answer[player2]+=abs(player1_force-player2_force)
            return player2,player1,answer
def round_main():
    global answer
    if curr_location[next_x][next_y]: #현재 위치에 다른 플레이어가 존재할 경우
        
        player2 = curr_location[next_x][next_y]

        winner,loser,answer = fight(player1,player2,answer)
        
        loser_direction = curr_direction[loser]
        
        player_location[winner] = [next_x,next_y]
        curr_location[next_x][next_y] = winner
        curr_location[x][y] = 0
        loser_move(loser,loser_direction,next_x,next_y)
        winner_move(winner,next_x,next_y)

    else: # 현재 위치에 아무도 없으므로 그냥 이동함 
        curr_location[next_x][next_y]=player1
        player_location[player1] =[next_x,next_y]
        curr_location[x][y] = 0
        if arr[next_x][next_y]:
            if gun[player1]<arr[next_x][next_y][-1]:
                arr[next_x][next_y].append(gun[player1])# 진사람은 현재 위치에 총을 버려야함 
                arr[next_x][next_y] = sorted(arr[next_x][next_y]) 
                gun[player1] = arr[next_x][next_y].pop()

    
n,m,k = map(int,input().split()) # grid size , players , rounds

arr = [[[] for _ in range(n)] for _ in range(n)]

answer = [0]*(m+1)
base_force = [0]*(m+1)
gun = [0]*(m+1)
curr_direction = [0]*(m+1) # 플레이어 번호를 넣으면 해당 플레이어의 방향을 알려줌
curr_location = [[0]*n for _ in range(n)] # 좌표를 넣으면 해당 좌표에 플레이어가 있는지 알려줌 
player_location = [0]*(m+1) # 플레이어 번호를 넣으면 해당 플레이어가 어느 좌표에 있는지 알려줌 

for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(n):
        arr[i][j].append(temp[j])

for player in range(1,m+1):
    x,y,d,s = map(int,input().split())
    x,y = x-1,y-1  # 좌표값 정규화

    curr_direction[player]=d
    base_force[player] = s
    curr_location[x][y] = player
    player_location[player] = [x,y]


for round in range(k):
    
    for player1 in range(1,m+1):
        x,y = player_location[player1]
        direction = curr_direction[player1]
        next_x,next_y = next_xy(direction,x,y)

        if 0<=next_x<n and 0<=next_y<n:
            round_main()
                    
        else: # 막다른 길이므로 정반대로 돌아야함 

            direction = reverse_direction(direction)
            curr_direction[player1] = direction
            next_x,next_y = next_xy(direction,x,y)

            if 0<=next_x<n and 0<=next_y<n:
                round_main()
    # print(player_location)

print(*answer[1:])
                

            
            

            

