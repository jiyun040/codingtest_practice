numbers = [int(input()) for _ in range(7)]

odd = []
for num in numbers:
    if num % 2 == 1:
        odd.append(num)

if odd:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)