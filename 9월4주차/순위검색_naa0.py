"""
getSubset : 되는 경우 다 담는 함수
ex) 첫 번째 info 경우
['java backend junior pizza', '- backend junior pizza', 'java - junior pizza', '- - junior pizza', 'java backend - pizza', '- backend - pizza', 'java - - pizza', '- - - pizza', 'java backend junior -', '- backend junior -', 'java - junior -', '- - junior -', 'java backend - -', '- backend - -', 'java - - -', '- - - -']

- combinations 쓰는 게 더 나을 듯
"""

def getSubset(arr):
    # 4
    _length = len(arr)
    result = []
    
    # 4자리에서 - 들어갈 수 있는 모든 경우의 수 구하기
    for i in range(1 << _length):
        temp = []
        for j in range(_length):
            if i & (1 << j):
                temp.append(j)
        temp_arr = arr[:]
        
        for idx in temp:
            temp_arr[idx] = '-'
            
        result.append(' '.join(temp_arr))
        
    return result

# 이분탐색 함수 (score 기준으로 arr 비교)
def getBinarySearch(score, arr):
    if not arr: return 0

    start, end = 0, len(arr)
    mid = (start + end) // 2

    """
    중간값이 타겟값보다 크거나 같으면
    끝 인덱스를 중간 인덱스로 옮기기
    """
    while start < end:
        mid = (start + end) // 2
        
        value = arr[mid]
        if value >= score:
            end = mid
        else:
            start = mid+1

    # 전체에서 끝 인덱스를 빼줘야 더 큰 경우가 나옴
    return len(arr) - end

from collections import defaultdict
def solution(info, query):
    answer = []
    answer_dict = defaultdict(list)
    
    # 지원자가 합격 가능한 쿼리문 전체 조회
    for _info in info:
        _info = _info.split(' ')
        for _subset in getSubset(_info[:-1]):
            # 각 쿼리 키의 값으로 점수 넣기
            answer_dict[_subset].append(int(_info[-1]))
            
    """
    최종 answer_dict
    defaultdict(<class 'list'>, {'java backend junior pizza': [150], '- backend junior pizza': [150], 'java - junior pizza': [150], '- - junior pizza': [150], 'java backend - pizza': [150], '- backend - pizza': [150, 260], ...
    """

    # dict value 정렬
    for _value in answer_dict.values():
        if _value:
            _value.sort()

    for _query in query:
        # ex) ['java', 'and', 'backend', 'and', 'junior', 'and', 'pizza', '100']
        q_list = _query.split(' ')
        
        # 점수 따로 빼주기
        score = int(q_list.pop())
        # and 제외한 부분들
        q_list = [q for idx, q in enumerate(q_list) if idx%2 == 0]
        # 최종 쿼리
        condition = ' '.join(q_list)
        # answer_dict.get(condition) => condition 쿼리문과 일치하는 부분 점수값들
        answer.append(getBinarySearch(score, answer_dict.get(condition)))

    return answer