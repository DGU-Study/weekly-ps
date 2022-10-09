'''
조이스틱으로 알파벳 이름을 완성하기

상: 다음 알파벳
하: 이전 알파벳
좌: 커서를 왼쪽으로 이동, 첫번째에서 이동하면 마지막으로 커서 이동
우: 커서를 오른쪽으로 이동, 마지막에서 이동하면 처음으로 커서 이동

처음 시작은 A*(문자길이)

조이스틱


'''
'''
def solution1(name):
    answer = 0
    name_len = len(name)

    answer = sum([min(abs(ord('A')-ord(n)), 26-abs(ord('A')-ord(n))) for n in name]) # 상하 움직임 합으로 초기화 
    min_move = name_len - 1 # 좌우 최소 움직임
    
    for i in range(name_len):
        nxt = i+1
        while nxt < len(name) and name[nxt] == 'A':
            nxt += 1
        min_move = min(min_move, 2*i + len(name) - nxt, i + 2*(len(name) - nxt))
    
    answer += min_move # 좌우 움직임 더하기
    return answer
'''

from collections import deque

# "A"*len(name)에서 주어진 name을 만들기 위해
# A가 아닌 곳을 바꾸기위해 최소로 움직이며 모두 방문하여 주어진 name과 일치하도록 만들어주어야한다.
# 역으로, 주어진 name이 모두 A가 되게하는 최소 이동거리를 구해준다. (굉장히 그리디...!)
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

testcase = ["JEROEN", 	"JAN"]
for name in testcase:
    print(solution(name))