import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = list(map(int,input().split()))

start,end = 0,0
start_answer = 10**6
answer = start_answer
temp = 0
ryan = 0

if arr[end] == 1:
    ryan += 1



while True :
    if ryan<k:
        if end<n-1:
            end += 1
            temp += 1

            if arr[end] == 1:
                ryan += 1
        else: # 더이상 갈 곳이 없으므로 
            break

    if ryan >= k:

        answer = min(answer,temp)
        
        if temp == k:
            break

        if arr[start] == 1:
            ryan -= 1

        start += 1
        temp = end-start + 1

    if start == end:
        if ryan>=k:
            answer = min(answer,temp)
            break

print(answer if answer!=start_answer else -1)