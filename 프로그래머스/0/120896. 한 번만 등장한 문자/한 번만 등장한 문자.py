def solution(s):
    answer = ''
    uniqueChars = (i for i in s if s.count(i) == 1)
    answer = ''.join(sorted(uniqueChars))     
    return answer