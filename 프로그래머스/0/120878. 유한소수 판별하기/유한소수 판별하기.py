import math

def solution(a, b):
    #최대공약수 gcd
    gcd = math.gcd(a, b)
    
    #기약분수 구하기
    b //= gcd
    
    #분모에서 2와 5 제거 -> 1인지 아닌지 구별
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    
    if b == 1:
        return 1
    else:
        return 2