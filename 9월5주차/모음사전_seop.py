
from collections import defaultdict



lis = ['A','E','I','O','U']
visited = defaultdict(int)
answer = 1

def loop(string,word):
        global answer
        global visited
        for i in lis:
            if visited[string+i] == 0:
                visited[string+i] = answer
                answer+=1
                if len(string) <= 3:
                    loop(string+i,word)

def solution(word):
    
    loop('',word)
    return visited[word]