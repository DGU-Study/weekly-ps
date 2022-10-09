from collections import deque

def bfs(name):
    q = deque([(list(name), 0, 0)])

    while q:
        name_list, lr_cnt, idx = q.popleft()
        name_list[idx]='A'

        if name_list.count('A') == len(name):
            return lr_cnt
        
        for i in [-1,1]:
            name_copy = name_list[:]
            q.append((name_copy, lr_cnt+1, idx+i))

def solution(name):
    up_cnt = sum([min(abs(ord('A')-ord(n)), 26-abs(ord('A')-ord(n))) for n in name])
    lr_cnt = bfs(name)
    return up_cnt + lr_cnt
