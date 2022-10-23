def find_root(root, n):
  if root[n] != n:
    root[n] = find_root(root, root[n])
  return root[n]

def union_node(root, n1, n2):
  n1 = find_root(root, n1)
  n2 = find_root(root, n2)
  if n1 > n2:
    root[n1] = n2
  else:
    root[n2] = n1


import sys
si = sys.stdin.readline

n = int(si()) # o
m = int(si()) # v

root = [i for i in range(n+1)] # 사이클 판별을 위한 루트 리스트
v_list = [] # 간선 정보 저장 리스트

for _ in range(m):
  a, b, cost = map(int, si().split()) 
  v_list.append((cost, a, b))

v_list.sort() # 비용 기준 오름차순 정렬

ans = 0
for cost, n1, n2 in v_list:
  if find_root(root, n1) != find_root(root, n2): # 사이클을 생성하지 않으면
    union_node(root, n1,n2) # 서로소 집합에 추가
    ans += cost

print(ans)