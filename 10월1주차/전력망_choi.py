from collections import deque

def bfs(tree, start, visited):
    q = deque([start])
    visited.append(start)
    while q:
        now = q.popleft()
        for nxt in tree[now]:
            if nxt not in visited:
                q.append(nxt)
                visited.append(nxt)
    return len(visited)

def solution(n, wires):

    answer = n

    for i in range(len(wires)):
        tree = [[] for _ in range(n)]
        for idx, wire in enumerate(wires):
            if idx==i:
                continue
            tree[wire[0]-1].append(wire[1]-1)
            tree[wire[1]-1].append(wire[0]-1)
        
        one = bfs(tree, 0, [])

        result = abs((n - one) - one)

        if answer > result:
            answer = result

    return answer