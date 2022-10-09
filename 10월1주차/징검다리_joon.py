def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance) #도착지까지의 거리 계산하기 위해 
    
    start, end = 0, distance 
    while start <= end:
        mid = (start + end) // 2
        current, remove = 0,0
        min_distance = float('INF')
        
        for rock in rocks:
            dist = rock - current #바위와 현재 위치와의 거리
            if dist < mid:
                remove += 1
            else:
                current = rock #현재 위치를 그 바위로 옮긴다
                min_distance = min(min_distance, dist) #해당 mid단계에서 최소 거리인지 체크
        
        if remove > n:
            end = mid - 1
        else:
            answer = min_distance
            start = mid + 1
    return answer