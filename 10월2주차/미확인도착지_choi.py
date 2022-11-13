'''


def dijkstraByAdjacencyList(graph, start):
    distances = {node: int(1e9) for node in graph}
    distances[start] = 0
    pq = []
    heapq.heappush(pq, [distances[start], start])

    while pq:
        current_distance, current_target = heapq.heappop(pq)
        if distances[current_target] < current_distance:
            continue
            
        for new_target, new_distance in graph[current_target].items():
            distance = current_distance + new_distance
            if distance < distances[new_target]:
                distances[new_target] = distance
                heapq.heappush(pq, [distance, new_target])

    return distances

import heapq
from collections import defaultdict
import sys
si = sys.stdin.readline

T = int(si())
for _ in range(T):
    n, m, t = map(int,si().split()) # 노드의 개수, 간선의 개수, 목적지의 개수
    s, g, h = map(int,si().split()) # 출발 노드, 지나간 두 노드

    graph = defaultdict(dict)
    for node in range(n+1): # 0(n) 2,000
        graph[node]
    for _ in range(m): # 0(n) 50,000
        a, b, d = map(int,si().split()) # 두 개의 노드와 그 사이 거리
        if (a == g and b == h) or (a == h and b == g):
            d -= 0.01
        graph[a][b] = d
        graph[b][a] = d

    # 목적지 리스트 초기화
    target_list = [int(si()) for _ in range(t)] # 0(n) 1,000

    s_distances = dijkstraByAdjacencyList(graph, s)
    answer = []
    for target in target_list:
        if isinstance(s_distances[target], float):
            answer.append(target)

    print(*sorted(answer))

'''

def dijkstraByAdjacencyList(graph, start):
    distances = {node: int(1e9) for node in graph}
    distances[start] = 0
    pq = []
    heapq.heappush(pq, [distances[start], start])

    while pq:
        current_distance, current_target = heapq.heappop(pq)
        if distances[current_target] < current_distance:
            continue
            
        for new_target, new_distance in graph[current_target].items():
            distance = current_distance + new_distance
            if distance < distances[new_target]:
                distances[new_target] = distance
                heapq.heappush(pq, [distance, new_target])
    return distances

import heapq
from collections import defaultdict
import sys
si = sys.stdin.readline

T = int(si())
for _ in range(T):
    n, m, t = map(int,si().split()) # 노드의 개수, 간선의 개수, 목적지의 개수
    s, g, h = map(int,si().split()) # 출발 노드, 지나간 두 노드

    graph = defaultdict(dict)
    for node in range(n+1): # 0(n) 2,000
        graph[node]
    for _ in range(m): # 0(n) 50,000
        a, b, d = map(int,si().split()) # 두 개의 노드와 그 사이 거리
        graph[a][b] = d
        graph[b][a] = d

    # 목적지 리스트 초기화
    target_list = [int(si()) for _ in range(t)] # 0(n) 1,000

    s_distances = dijkstraByAdjacencyList(graph, s)


    gh_distance = graph[h][g]

    # 중복된 이동을 제거하기 위해 필수 통로 제거
    graph[g].pop(h)
    graph[h].pop(g)

    answer = []
    for target in target_list:
        target_distances = dijkstraByAdjacencyList(graph, target)
        if s_distances[target] >=  min(s_distances[g] + gh_distance + target_distances[h], s_distances[h] + gh_distance + target_distances[g]): # s-g-h-목적지 거리가 최단거리보다 작거나 같으면 가능
             answer.append(target)

    print(*sorted(answer))