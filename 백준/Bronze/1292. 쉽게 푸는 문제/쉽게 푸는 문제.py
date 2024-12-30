A, B = map(int, input().split()) #입력받기

#수열 생성
sequence = []
for i in range(1, 50): #적당히 생성
    sequence.extend([i] * i) #i를 i번 반복해 리스트에 iterable의 형태로 추가

#구간 추출 및 합
    result = sum(sequence[A - 1:B]) #A번째부터 B번째가지의 합

print(result)