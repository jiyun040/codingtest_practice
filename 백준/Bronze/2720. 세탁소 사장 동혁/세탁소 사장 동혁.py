# 쿼터: 25센트
# 다임: 10센트
# 니켈: 5센트
# 페니: 1센트

T = int(input())
test_case = [int(input()) for _ in range(T)]

coins = [25, 10, 5, 1]

#C는 각 동전의 개수를 저장
for C in test_case:
    result = []
    for coin in coins:
        result.append(C // coin)
        C %= coin
    print(*result)
# *를 붙이는 이유: 개별로 하나씩 출력하기 위해서, 리스트를 언패킹 한다.