from itertools import product

def solution(word):

    alphabet = ['A','E','I','O','U']
    all_word = []
    for i in range(1,6):
        for p in product(alphabet,repeat=i):
            p = ''.join(p)
            all_word.append(p)

    all_word.sort()

    return all_word.index(word)+1

testcase = ["AAAAE","AAAE","I","EIO"]

for word in testcase:
    print(solution(word))