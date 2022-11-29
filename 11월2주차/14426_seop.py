import sys
from collections import defaultdict
input = sys.stdin.readline
n,m = map(int,input().split())

string_box = [input().strip() for _ in range(n)]

answer = 0


for _ in range(m):
    string = input().strip()
    for sb in string_box:
        if sb[:len(string)] == string:
            answer += 1 
            break


print(answer)