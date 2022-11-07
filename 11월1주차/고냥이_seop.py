def solution(n,arr):
    from collections import defaultdict 

    dic = defaultdict(int)

    visited = []
    cnt = 1
    answer = 0

    current = 1

    start, end = 0, 0
    visited.append(arr[start])

    for _ in range(len(arr)):

        answer = max(current,answer)
        
        
        if end < len(arr)-1: #끝점에 가면 더이상 움직이지 않아도 되므로 
            end+=1
            if arr[end] not in visited:
                cnt+=1
            visited.append(arr[end])
            current+=1
        
        if cnt>n:
      
            while True:
                
               
                if visited.count(arr[start]) == 1:
                    visited.remove(arr[start])
                    cnt-=1
                    current-=1
                    start += 1 
                    break

                else:
                    visited.remove(arr[start])
                    current -=1
                    start += 1
            

    return answer            
        


import sys
input = sys.stdin.readline 

n = int(input())
arr = list(input().strip())

answer = solution(n,arr)

print(answer)

