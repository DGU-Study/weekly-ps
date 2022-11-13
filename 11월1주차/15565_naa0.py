# 입력 테스트용
import os
currentPath = os.getcwd()
os.chdir(currentPath)
print(currentPath)
import sys
sys.stdin = open(currentPath + "/11월1주차/백준_15565.txt", "r")

# 입력 값 받기
n, k = map(int, input().split())
data = list(map(int, input().split()))
ans = float('inf')

# 끝 포인터, 라이언 개수, 선택인형 개수
end, cnt, dolls = 0, 0, 0

for start in range(n):
    # end를 가능한 만큼 이동시키기
    while cnt < k and end < n:
        dolls += 1
        # 라이언 있을 때 카운트 증가
        if data[end] == 1:
            cnt += 1
        end += 1
        
    if cnt == k and ans > dolls:
        ans = dolls

    if data[start] == 1:
        cnt -= 1

    # start가 하나 움직여서 전체 수 줄어듦    
    dolls -= 1
    

print(ans if ans != float('inf') else -1)
