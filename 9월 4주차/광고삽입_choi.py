def strTosec(s):
    return int(s[:2])*3600 + int(s[3:5])*60 + int(s[6:]) 

def secTostr(n):
    return f'{str(n//3600).zfill(2)}:{str((n%3600)//60).zfill(2)}:{str((n%3600)%60).zfill(2)}'

def solution(play_time, adv_time, logs):

    play_sec = strTosec(play_time)
    adv_sec = strTosec(adv_time)

    view = [0 for _ in range(play_sec+1)]

    for log in logs:
        start_sec = strTosec(log[:8])
        end_sec = strTosec(log[9:])
        view[start_sec] +=1
        view[end_sec] -=1

    for i in range(1, len(view)):
        view[i] += view[i-1]

    for i in range(1, len(view)):
        view[i] += view[i-1]

    max_view = view[adv_sec-1]
    answer = 0

    for i in range(adv_sec, play_sec):
        tmp = view[i]-view[i-adv_sec]
        if max_view < tmp:
            max_view = tmp
            answer = i-adv_sec+1

    return secTostr(answer)


testcase = [["02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]]
    ,["99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]]
    ,["50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]]]


for play_time, adv_time, logs in testcase:
    print(solution(play_time, adv_time, logs))
