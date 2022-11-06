def find_parent(parent, univ):
    if parent[univ] != univ:
        parent[univ] = find_parent(parent, parent[univ])
    return parent[univ]

def union_parent(parent, univ1, univ2):
    univ1 = find_parent(parent, univ1)
    univ2 = find_parent(parent, univ2)
    if univ1 > univ2:
        parent[univ1] = univ2
    else:
        parent[univ2] = univ1

import sys
si = sys.stdin.readline

n, m = map(int, si().split()) # o, v

parent = [univ for univ in range(n+1)] # 부모노드 정보 초기화
univ_dic = {univ:info for univ, info in enumerate(si().split(), start=1)} # 대학교 정보 초기화

v_list = [] # 간선 정보 초기화
for _ in range(m): 
    u, v, d = map(int,si().split())
    v_list.append((d, u, v))

v_list.sort() # 거리순 오름 차순 정렬

ans = 0
cnt = 0
for d, u, v in v_list:
    if (find_parent(parent, u) != find_parent(parent, v)) and (univ_dic[u] != univ_dic[v]): # 사이클을 만들지 않는 간선, 남초-여초 대학인 경우
        union_parent(parent, u, v)
        ans += d
        cnt +=1
    if cnt == n-1:
        break

if cnt!=n-1:
    ans = -1

print(ans)