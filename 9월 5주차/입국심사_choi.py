def solution(n, times):
    answer = 0

    left = 0
    right = max(times)*n

    while left <= right:
        mid = (left + right) // 2
        boarded = 0
        for time in times:
            boarded += mid//time
        if boarded >= n:
            right = mid - 1
        else:
            left = mid +1
    answer = left
    return answer

testcase =  [[6, [7,10]]]
for n, times in testcase:
    print(solution(n, times))