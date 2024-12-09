N = int(input()) #길이 입력받기
OX = input() #OX 입력받기

score = 0
bonus = 0

for i in range(len(OX)): #OX의 길이 만큼 반복
    if OX[i] == 'O': #만약 맞았다면 
        score += i + 1 + bonus
        bonus += 1
    else: #틀렸다면 보너스 점수 초기화
        bonus = 0

print(score)