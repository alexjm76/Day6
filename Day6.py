def factorial_iter(n):
    """
    반복문을 사용한 팩토리얼 함수
    :param n: n!
    :return: integer ㅠㅐㄱ토리얼 계산 결과 값
    """
    result = 1
    for k in range(1, n+1):
        result = result*k
    return  result

def factorial_recu(n):
    """
    재귀 함수를 사용한 팩토리얼 함수
    :param n: n!
    :return:  자기 자신을 호출 또는 1
    """
    if n == 1: #끝나는 조건
        return 1
    else:
        return factorial_recu(n-1) * n
    
    
def somethin(n):
    a=5+n #전역 변수는 바꾸면 바뀌는데 로컬 함수는 바꿔도 안바뀜
    print(a)
    
    
print(factorial_recu(5))
print(factorial_iter(5))