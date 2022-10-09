def solution(distance, rocks, n):

    answer = 0
    rock_list = sorted(rocks) + [distance] 

    low = 0
    high = distance
    idx=0

    while low <= high:
        mid = (low+high)//2
        current = 0
        remove = 0 
        min_diff = distance
        
        idx += 1
        for rock in rock_list:
            diff = rock - current 
            if diff >= mid:
                current = rock
                min_diff = min(min_diff, diff)
            else:
                remove += 1
                
        if remove > n:
            high = mid -1
        else:
            low = mid + 1 
            answer = min_diff
            
    return answer