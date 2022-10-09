def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    
    low = 0 
    high = distance 
    
    
    weight = 0 
    while low<=high:
        
        mid = (high+low) // 2
        cnt_rock = 0 
        start,weight = 0,0
        
        for i in range(len(rocks)):
            
            if rocks[i] - start <mid:
                cnt_rock += 1        
            else:
                start = rocks[i]
            
            if cnt_rock> n:
                break
        
        if cnt_rock > n: 
            high = mid-1 
        else:
            answer = max(answer,mid)
            low = mid+1
            
                
            
            
    return answer