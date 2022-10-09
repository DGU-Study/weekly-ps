def solution(distance, rocks, n):

    answer = 0
    rock_list = sorted(rocks) + [distance] # 50,000

    low = 0
    high = distance
    idx=0

    while low <= high: # log2(50,000) = 약 16
        mid = (low+high)//2
        current = 0
        remove = 0 
        
        idx += 1
        for rock in rock_list:
            diff = rock - current 
            if diff >= mid:
                current = rock
            else:
                remove += 1
                
        if remove > n:
            high = mid -1
        else:
            low = mid + 1 
            answer = mid 

    return answer