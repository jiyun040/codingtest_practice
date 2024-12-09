def solution(my_string):
    my_string = my_string.lower()
    sortedString = sorted(my_string)
    answer = ''.join(sortedString)
    return answer
