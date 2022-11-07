# 입력 테스트용
import os
currentPath = os.getcwd()
os.chdir(currentPath)
print(currentPath)
import sys
sys.stdin = open(currentPath + "/11월1주차/백준_16472.txt", "r")

for _ in range(4):
    # 입력 값 받기
    n = int(input())
    data = input()
    # 끝 포인터
    end = 1
    # 문자열 길이
    N = len(data)
    # 정답
    ans = 0

    from collections import deque

    # 각 알파벳 마지막 인덱스
    alphabet_dict = dict()

    for start in range(N):
        if data[start] in alphabet_dict.keys():
            alphabet_dict[data[start]] += 1
        else:
            alphabet_dict.setdefault(data[start], 0)

        while len(alphabet_dict) <= n and end < N:
            if data[end] in alphabet_dict.keys():
                alphabet_dict[data[end]] += 1
            else:
                alphabet_dict[data[end]] = 0
            end += 1

        ans = max(ans, end - start)

        # start는 다음 반복문때 빠짐
        alphabet_dict[data[start]] -= 1
        if not alphabet_dict[data[start]]:
            del alphabet_dict[data[start]]

    print(ans)
