from distutils.util import strtobool


def strTosec(s):
    return int(s[:2])*60*60 + int(s[3:5])*60 + int(s[6:]) 

def secTostr(n):
    return f'{str(n%60).zfill(2)}:{str(n/60%60).zfill(2)}:{str(n/60/60).zfill(2)}'

def solution(play_time, adv_time, logs):
    answer = ''



    for log in logs:
        start_sec = strTosec(log[:8])
        end_sec = strTosec(log[9:])
        print(log, start_sec,end_sec)
        #for sec in range(start_sec,end_sec):
        #    print(0)

    play_sec = strTosec(play_time)
    adv_sec = strTosec(adv_time)
    print(play_sec,adv_sec)

    

    return answer


testcase = [["02:03:55",	"00:14:15",	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]]
    ,["99:59:59",	"25:00:00",	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]]
    ,["50:00:00",	"50:00:00",	["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]]]

for play_time, adv_time, logs in testcase:
    solution(play_time, adv_time, logs)
