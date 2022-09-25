'''
첫번째 풀이 
채점 결과
정확성: 40.0
효율성: 0.0
합계: 40.0 / 100.0

def solution(info, query):
    answer=[]
    
    info_dic = dict()
    for i in info:
        tmp_info = list(i.split())
        if tmp_info[-1] in info_dic:
            info_dic[tmp_info[-1]].append(tmp_info[:-1])
        else:
            info_dic[tmp_info[-1]] = [tmp_info[:-1]]

    for q in query:
        cnt=0
        q_list = list(q.replace("and"," ").split())
        for key in info_dic:
            if int(key) >= int(q_list[-1]):
                for value in info_dic[key]:
                    flag = 1
                    for q_v in q_list[:-1]:
                        if q_v!="-" and (q_v  not in value):
                            flag = 0
                    if flag:
                        cnt+=1
        answer.append(cnt)     
    return answer
'''

'''
두번째 풀이
채점 결과
정확성: 40.0
효율성: 0.0
합계: 40.0 / 100.0

from collections import defaultdict

def solution(info, query):
    answer=[]
    info_dic = defaultdict(lambda: list())

    for i in info:
        i_lst = list(i.split())

        i_group = [f'{i_lst[0]} and {i_lst[1]} and {i_lst[2]} and {i_lst[3]}'
                    ,f'- and {i_lst[1]} and {i_lst[2]} and {i_lst[3]}'
                    ,f'{i_lst[0]} and - and {i_lst[2]} and {i_lst[3]}'
                    ,f'{i_lst[0]} and {i_lst[1]} and - and {i_lst[3]}'
                    ,f'{i_lst[0]} and {i_lst[1]} and {i_lst[2]} and -'
                    ,f'{i_lst[0]} and {i_lst[1]} and {i_lst[2]} and -'
                    ,f'- and - and {i_lst[2]} and {i_lst[3]}'
                    ,f'- and {i_lst[1]} and - and {i_lst[3]}'
                    ,f'- and {i_lst[1]} and {i_lst[2]} and -'
                    ,f'{i_lst[0]} and - and - and {i_lst[3]}'
                    ,f'{i_lst[0]} and - and {i_lst[2]} and -'
                    ,f'{i_lst[0]} and {i_lst[1]} and - and -'
                    ,f'{i_lst[0]} and - and - and -'
                    ,f'- and {i_lst[1]} and - and -'
                    ,f'- and - and {i_lst[2]} and -'
                    ,f'- and - and - and {i_lst[3]}'
                    ,f'- and - and - and -']

        info_dic[i_lst[4]].append(i_group)


    for q in query:
        q_list = list(q.replace('and','').split())
        cnt=0
        for key in info_dic:
            if int(key) >= int(q_list[4]):
                for i_group in info_dic[key]:
                    if f'{q_list[0]} and {q_list[1]} and {q_list[2]} and {q_list[3]}'in i_group:
                        cnt+=1
        answer.append(cnt) 
    return answer
'''

'''
세번째 풀이
채점 결과
정확성: 40.0
효율성: 0.0
합계: 40.0 / 100.0

from collections import defaultdict

def lbbs(list, target):
    '''
    lower bound binary search
    쿼리 값 이상을 찾기 위함으로
    '''
    left=0
    right=len(list)
    while left<right:
        mid = (left+right)//2
        if target <= list[mid]:
            right = mid
        else:
            left = mid + 1
    return left


def solution(info, query):
    answer=[]
    info_dic = defaultdict(lambda: list())

    for i in info:
        i_lst = list(i.split())

        i_group = [f'{i_lst[0]} and {i_lst[1]} and {i_lst[2]} and {i_lst[3]}'
                    ,f'- and {i_lst[1]} and {i_lst[2]} and {i_lst[3]}'
                    ,f'{i_lst[0]} and - and {i_lst[2]} and {i_lst[3]}'
                    ,f'{i_lst[0]} and {i_lst[1]} and - and {i_lst[3]}'
                    ,f'{i_lst[0]} and {i_lst[1]} and {i_lst[2]} and -'
                    ,f'{i_lst[0]} and {i_lst[1]} and {i_lst[2]} and -'
                    ,f'- and - and {i_lst[2]} and {i_lst[3]}'
                    ,f'- and {i_lst[1]} and - and {i_lst[3]}'
                    ,f'- and {i_lst[1]} and {i_lst[2]} and -'
                    ,f'{i_lst[0]} and - and - and {i_lst[3]}'
                    ,f'{i_lst[0]} and - and {i_lst[2]} and -'
                    ,f'{i_lst[0]} and {i_lst[1]} and - and -'
                    ,f'{i_lst[0]} and - and - and -'
                    ,f'- and {i_lst[1]} and - and -'
                    ,f'- and - and {i_lst[2]} and -'
                    ,f'- and - and - and {i_lst[3]}'
                    ,f'- and - and - and -']

        info_dic[int(i_lst[4])].append(i_group)


    info_keys = sorted(info_dic.keys())

    for q in query:
        q_list = list(q.replace('and','').split())
        cnt=0

        min_key_idx = lbbs(info_keys, int(q_list[4]))

        for key in info_keys[min_key_idx:]:
            for i_group in info_dic[key]:
                if f'{q_list[0]} and {q_list[1]} and {q_list[2]} and {q_list[3]}'in i_group:
                    cnt+=1
        answer.append(cnt) 
    return answer
'''

from collections import defaultdict

def solution(info, query):
    answer = []
    info_group = defaultdict(lambda: list())
    for i in info:
        info_group[].append()
    

    return answer







testcase = [[["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
            ,["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]]]

for info, query in testcase:
    solution(info, query) 
    