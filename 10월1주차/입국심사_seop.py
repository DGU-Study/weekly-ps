def solution(n,times):
    times = sorted(times)
    M = max(times)*n
    m = 0
    answer = 0

    while m<=M:
        mid = (M+m)//2
        numbers = 0

        for time in times:
            numbers += (mid//time)

            if numbers>=n:
                M = mid-1
                answer = mid 
                break
        if numbers<n:
            m = mid+1
    
    return answer