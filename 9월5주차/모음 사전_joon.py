def solution(word):
    answer = 0 
    letters = ['A', "E", "I", "O", 'U', ""]
    dic = dict()
    for i in range(5):
        for j in range(6):
            for k in range(6):
                for m in range(6):
                    for n in range(6):
                        dic[letters[i] + letters[j]+letters[k]+letters[m]+letters[n]] = 0
    for idx, val in enumerate(sorted(dic.keys())):
        if val == word:
            answer = idx+1
            break
    return answer