#햄버거와 음료 저장할 리스트 만들기
hamburger = []
beverage = []
for i in range(5):
    price = int(input())
    if i < 3: #처음 3개는 햄버거
        hamburger.append(price)
    else: #나머지 2개는 음료
        beverage.append(price)
#햄버거와 음료를 오름차순으로 정리
hamburger.sort()
beverage.sort()
#가장 저렴한 둘을 더한 후 50 빼기
print(hamburger[0] + beverage[0] - 50)