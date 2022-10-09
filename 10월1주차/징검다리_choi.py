'''
출발지점부터 distance만큼 떨어진 곳에 도착지점

그 사이에는 바위

바위 중 n개를 제거
'''

'''
from itertools import combinations

def solution(distance, rocks, n):

    answer = 0
    for case in combinations(rocks, len(rocks)-n): # 50,000
        rock_list = [0] + sorted(case) + [distance] # 50,000
        diff_list = [r2-r1 for r1, r2 in zip(rock_list, rock_list[1:])] # 50,000

        min = sorted(diff_list, reverse=True).pop() # 50,000
        if answer < min:
            answer = min
    return answer
'''
'''
문제가 상당히 어렵다.

너무나 익숙한 접근법으로는 n개를 지울 수 있는 모든 경우를 조합으로 구하여
모든 케이스에 대한 가장 작은 차이값 중 가장큰 값을 출력할 것이다. 

하지만, 문제에서 주어진 것처럼 바위의 개수는 5만개이며 시작과 끝의 차이는 10억이다.

5만개의 바위에서 n개를 제거한 조합을 찾는 시간복잡도는 5만이며
모든 케이스의 차이값을 탐색하기위해서는 5만*5만 이상이 소요된다. 
따라서, 이 문제는 완전 탐색으로 접근하면 효율성 TC에 의해서 통과하지 못한다.

따라서, 이분탐색으로 문제를 접근해본다.
이분탐색으로 접근하게된다면 10억도 30번이면 탐색이 가능하고, 5만은 16번이면 탐색가능하다.

그래서, 어떻게 풀이를 해야하나?

우리가 찾는 값은 바위 n개를 제거했을 때 각 바위 사이의 거리를 측정하여 나온 최소거리 중에서 최대값이다.
따라서, 이분 탐색으로 찾는 값을 바위를 지우기 위한 최소 간격으로 설정하고 문제를 접근해 보아야 한다.

투 포인터를 통해 최소간격보다 작은 경우 해당 바위를 지워줍니다. (시간복잡도 : len(rocks) => 5만)

지워진 바위의 개수가 n보다 크면 상한값을 축소(최소 간격을 감소)시키고,
지워진 바위의 개수가 n이하이면 하한값을 축소(최소 간격을 증가)시킵니다. 

그렇게 n개를 지우는 최소 간격 중 최대 값



'''
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
        min_diff = distance
        
        idx += 1
        for rock in rock_list:
            diff = rock - current 
            if diff >= mid:
                current = rock
                min_diff = min(min_diff, diff) # mid(바위사이간격)을 만족할 때 최소 거리를 저장해둔다.
            else:
                remove += 1
                
        if remove > n:
            high = mid -1
        else:
            low = mid + 1 
            answer = min_diff # 조건을 만족하는 최소거리 중 최대 값을 갱신

    return answer

testcase = [[25, [2, 14, 11, 21, 17], 2]]

for distance, rocks, n in testcase:
    print(solution(distance, rocks, n))