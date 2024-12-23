x = int(input())  #총 금액
n = int(input())  #품목 개수
sum = 0

for _ in range(n):
    a, b = map(int, input().split())  # 품목의 가격과 개수 입력
    sum += a * b  #총합

if x == sum:
    print("Yes")
else:
    print("No")
