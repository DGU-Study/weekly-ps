# 1~1e5 길이의 문자열이 주어진다.
# 문자열에는 알파벳 소문자만이 포함된다.
# 문자열 중에서 최대 N개의 종류의 알파벳을 가진 연속된 문자열만을 인식할 수 있다.
# 인식할 수 있는 최대 문자열의 길이를 구한다.

import sys
si =sys.stdin.readline

N = int(si())
s = si().strip()

R=-1
cnt = [0]*26 # 알파벳별로 카운팅
kind = 0 # 알파벳 종류 카운팅

ans = 0
L=0
for R in range(len(s)):
    r = ord(s[R])-ord('a')
    cnt[r]+=1
    if cnt[r]==1:
        kind+=1

    while kind > N: # 종류가 많아지면 왼쪽 이동하여 범위조정
        l = ord(s[L])-ord('a')
        cnt[l]-=1
        if cnt[l]==0:
            kind-=1
        L+=1
    
    ans=max(ans,R-L+1)

print(ans)