def solution(n, times):
    answer = 0
    times.sort()
    left = 0
    right = times[-1] * n #최대시간 
    
    while left <= right:
        mid = (left + right) // 2
        people = 0
        
        for time in times:
            people += mid // time # 검사 가능한 사람의 수 
            if n < people: #mid를 줄여도 됨
                break
        
        if n <= people:
            answer = mid
            right = mid - 1
        elif n > people: 
            left = mid + 1 
            
    return answer