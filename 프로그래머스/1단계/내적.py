# 프로그래머스 1단계 - 내적
def solution(a,b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer

def solution(a, b):
    
    return sum([x*y for x, y in zip(a,b)])