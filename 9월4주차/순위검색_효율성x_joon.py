def solution(info, query):
    answer = []
    new_info = []
    new_query = []
    
    for i in info:
        new_info.append(i.split(' '))
        new_info[-1][-1] = int(new_info[-1][-1])
        
    for i in query:
        tmp = i.split(' and ')
        a,b = tmp[-1].split(' ')
        tmp[-1] = a
        tmp.append(int(b))
        new_query.append(tmp)
        
    for i in new_query:
        cnt = 0
        for j in new_info:
            j_cnt = 0
            if i[-1] <= j[-1]:
                for k in range(4):
                    if j[k] == i[k] or i[k] == '-':
                        j_cnt += 1
                        
            if j_cnt == 4:
                cnt += 1
        answer.append(cnt)
    return answer