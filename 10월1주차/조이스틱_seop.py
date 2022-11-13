def solution(name):
    from collections import deque
    from copy import deepcopy
    alphabet =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    dic = {}
    start_string = 'A'*len(name)
    for idx, ab in enumerate(alphabet):
        dic[ab] = idx

    ud_cnt = 0
    for idx,lst in enumerate(zip(name,start_string)):
        i,j = lst[0],lst[1]
        
        tmp_cnt = min(abs(dic[i]-dic[j]) , abs(len(dic)-abs(dic[i]-dic[j])) )
        ud_cnt+= tmp_cnt # 위 아래로 커서를 누르는 횟수 
    
    def bfs(name):
        name_lst = list(name)    
        name_lst[0] = 'A'
        d = deque()
        d.append([name_lst,ud_cnt,0]) # lst,cnt,inx

        while d:
            
            arr,cnt,idx = d.popleft()
            arr[idx] = 'A'
            if arr.count('A') == len(name):
                return cnt
            
            for i in [-1,1]:
                
                new_arr = deepcopy(arr)
                
                d.append([new_arr,cnt+1,idx+i])
                
        
    return bfs(name)