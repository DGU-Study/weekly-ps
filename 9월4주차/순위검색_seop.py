def solution(infos, queries):
    from collections import defaultdict

    total_dic = defaultdict(list)
    # food_dic,age_dic,sort_dic = defaultdict(list),defaultdict(list),defaultdict(list)

    for info in infos:
            info = info.split(" ")
            for lang in [info[0], "-"]:
                for job in [info[1], "-"]:
                    for career in [info[2], "-"]:
                        for food in [info[3], "-"]:
                            total_dic[lang + job + career + food].append(int(info[4]))


    answer = []
    for key in total_dic:
        total_dic[key] = sorted(total_dic[key])
        
    for q in queries:
        q = q.split()
        lang,job,career,food,score = q[0],q[2],q[4],q[6],q[7]
        lis = total_dic[lang+job+career+food]
        s,h = 0,len(lis)

        mid = 0
        while s<h:
            mid = (s+h)//2      
            if lis[mid] >= int(score):
                h = mid 
            else:
                s = mid+1

        cnt = len(lis)-s

        answer.append(cnt)
    return answer