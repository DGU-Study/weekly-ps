import heapq

def dijkstra(n, s, graph):
    # 최단 거리 배열
    d = [float('inf')] * (n+1)
    d[s] = 0

    # 최소 힙
    hq = []
    heapq.heappush(hq, [0,s])

    while hq:
        tmp = heapq.heappop(hq)
        cost = tmp[0]
        node = tmp[1]

        if cost > d[node]:
            continue

        for v in graph[node]:
            neighbor = v[0]
            n_cost = d[node] + v[1]

            if n_cost < d[neighbor]:
                d[neighbor] = n_cost
                heapq.heappush(hq, [n_cost, neighbor])

    return d 

# main
T = int(input())

for _T in range(T):
    n, m, t = [int(x) for x in input().split()]
    s, g, h = [int(x) for x in input().split()]

    # 그래프 입력
    graph = [[] for _ in range(n+1)]
    for _m in range(m):
        a, b, d = [int(x) for x in input().split()]
        graph[a].append([b,d])
        graph[b].append([a,d])

        if (a == g and b == h) or (a == h and b == g):
            d_hg = d    # h와 g 사이의 거리

    targets = []
    for _ in range(t):
        targets.append(int(input()))
    targets.sort()

    # s에서 시작하는 최단경로 배열
    d_s = dijkstra(n,s,graph)
    # g에서 시작하는 최단경로 배열
    d_g = dijkstra(n,g,graph)
    # h에서 시작하는 최단경로 배열
    d_h = dijkstra(n,h,graph)

    for target in targets:
        if d_s[target] == d_s[g] + d_hg + d_h[target] or d_s[target] == d_s[h] + d_hg + d_g[target]:
            print(target, end=' ')
    print()