# 라이언, 어피치 인형 N개가 일렬로 놓여있다.
# 라이언은 1, 어피치는 2로 표현된다.
# 라이언 인형이 K개 이상 있는 가장 작은 연속된 인형들의 집합의 크기를 구한다.

# N과 K는 1~1e6
# 백만개의 인형 배열에서 연속된 집합의 크기를 찾기

import sys
si = sys.stdin.readline

N,K = map(int,si().split()) # 인형의 개수, 라이언 인형 조건
A = list(map(int,si().split())) # N개의 인형 배열

R=-1 # 라이언 인형 K개를 포함하는 집합의 오른쪽
cnt = 0 # 라이언 인형의 개수 카운팅
ans = -1
for L in range(N): # 라이언 인형 K개를 포함하는 집합의 왼쪽 
    while R+1<N and cnt<K:
        R+=1
        if A[R]==1: # 라이언 인형 수 카운팅
            cnt += 1
    if cnt==K: # 인형 수가 K개가 될 때
        if ans == -1:
            ans = R-L+1
        ans = min(ans, R-L+1)
    if A[L]==1: 
        cnt-=1
print(ans)