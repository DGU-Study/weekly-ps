#   시간 -> 초
def hourToSec(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def secToHour(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s

def solution(play_time, adv_time, logs):
    play_time = hourToSec(play_time)
    adv_time = hourToSec(adv_time)               
    # 특정 초에  시청하는 사람 수
    watch_time = [0 for i in range(play_time + 1)]

    for log in logs:
        start, end = log.split('-')
        start = hourToSec(start)
        end = hourToSec(end)
        # 보기 시작했을 때 시청자 수 +1명 
        watch_time[start] += 1
        # 보기 종료했을 때 시청자 수 -1명
        watch_time[end] -= 1
    
    # 시작, 끝 값 +1, -1 기준으로 사이값 채우기
    for w in range(1, len(watch_time)):
        watch_time[w] = watch_time[w] + watch_time[w - 1]

    # 사이값 채웠으면, 모든 시청자 수 누적해서 쌓아주기
    for w in range(1, len(watch_time)):
        watch_time[w] = watch_time[w] + watch_time[w - 1]

    tmp = 0
    max_time = 0
    for _time in range(play_time - adv_time + 1):
        # 특정 구간에서 누적 시청자수 최대 구간 어디인 지 구하기
        if watch_time[_time + adv_time] - watch_time[_time] > tmp:
            max_time = _time
            tmp = watch_time[_time + adv_time] - watch_time[_time]

    return secToHour(max_time + 1 if max_time else max_time)