# 두 수의 합 
n = int(input())
arr = list(map(int,input().split()))
x = int(input())

start, end = 0, n-1
cnt = 0

arr.sort()

for i in range(n):
  while arr[start] + arr[end] < x and start < n-1:
    start += 1
  while arr[start] + arr[end] > x and end > 1:
    end -= 1
  if start > end :
    break
  if arr[start] + arr[end] == x:
    cnt += 1
    end -= 1
    start += 1
print(cnt)