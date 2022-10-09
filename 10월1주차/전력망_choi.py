'''
n: 100 개의 송전탑 
wires: 99개의 전선 정보

트리 형태임으로 
n은 노드의 개수
wires은 간선의 개수이다

'''
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

testcase = [[9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]],
            [4,	[[1,2],[2,3],[3,4]]],
            [7,	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]]]

for n, wires in testcase:
	print(solution(n, wires))