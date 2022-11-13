def bfs():

    d = deque()
    d.append([0,string])
    
    visited = defaultdict(int)
    visited[string] = 1

    while d:
        cnt,s = d.popleft() 

        if len(set(s.strip('a'))) in [0,1]:
            print(cnt)
            break

        a_list,b_list = [], [] 
        
        for i in range(len(s)):
            
            if s[i] == 'a':
                a_list.append(i)
            else:
                b_list.append(i)

        for a in a_list:
            for b in b_list:

                new_string = list(s)
            
                temp1,temp2 = s[a],s[b]

                new_string[b] = temp1 
                new_string[a] = temp2

                new_string = ''.join(new_string)

                if not visited[new_string]:
                    visited[new_string] = 1
                    d.append([cnt+1,new_string])

import sys
from collections import defaultdict,deque
input=sys.stdin.readline 

string = (input().strip())
bfs()







