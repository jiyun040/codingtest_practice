#수열 B의 규칙: 더한 후 해당 인덱스의 값으로 나눔, 인덱스는 1부터 시작

N = int(input()) #입력받기
nums = [int(x) for x in input().split(' ')] #입력 받은 값들을 공백으로 구분 해 저장
result = [] 
result.append(nums[0]) #리스트의 초깃값 설정

total = 0

for i in range(2, N + 1): #첫번째는 했으니까 두번째 부터 시작
    total += result[-1] #이전까지 계산된 result의 값을 누적해서 더함
    x = int(nums[i - 1] * i - total) #i가 2부터 시작하기에 1을 빼줘야 함
    result.append(x)

for i in result:
    print(i, end = ' ')