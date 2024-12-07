def solution(num, k):
    Num = str(num)
    if str(k) in Num:
        return Num.index(str(k)) + 1
    else:
        return -1