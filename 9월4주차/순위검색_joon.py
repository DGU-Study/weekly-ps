from collections import defaultdict

def solution(info, query):
    score_dict = defaultdict(list)
    answer = [0] * len(query) 
    for i in range(len(info)):
        a, b, c, d, score = info[i].split()
        score = int(score)
        a_list = [a, '-']
        b_list = [b, '-']
        c_list = [c, '-']
        d_list = [d, '-']
        for q in range(2): # 하나의 info 통해 매칭될 수 있는 모든 경우의 수에다 점수 추가 
            for w in range(2):
                for e in range(2):
                    for r in range(2):
                        name = a_list[q] + b_list[w] + c_list[e] + d_list[r]
                        score_dict[name].append(score)

    for key in score_dict.keys(): #이진 탐색을 하기 위한 정렬
        score_dict[key].sort()
    
    for i in range(len(query)): #query를 돌면서 상응하는 key값의 score_list 찾기 
        query_list = list(query[i].split())
        score = int(query_list.pop(-1))
        for _ in range(3):
            query_list.remove('and')
        
        Q = "".join(query_list)
        
        score_list = score_dict[Q]
        if len(score_list) > 0:     #이진 탐색 
            left = 0
            right = len(score_list)
            while left < right:
                mid = (left + right) // 2
                if score_list[mid] >= score:
                    right = mid
                else:
                    left = mid+1
            answer[i] = len(score_list) - left
        else:
            answer[i] = 0
                
    return answer