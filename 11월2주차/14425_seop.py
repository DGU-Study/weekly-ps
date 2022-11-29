import sys
from collections import defaultdict
input = sys.stdin.readline
n,m = map(int,input().split())

visited = defaultdict(int)
string_box = []
for _ in range(n):
    string = input().strip()
    visited[string] = 1

answer = 0


for _ in range(m):
    string = input().strip()

    if visited[string] == 1:
        answer += 1 


print(answer)


