date = int(input())
car = list(map(int, input().split()))
violation = 0

for car_number in car:
    if car_number == date:
        violation += 1

print(violation)