num1 = int(input())
num2 = int(input())

one = num2 % 10
ten = (num2 // 10) % 10
hundred = num2 // 100

result1 = num1 * one
result2 = num1 * ten
result3 = num1 * hundred
result4 = num1 * num2

print(result1)
print(result2)
print(result3)
print(result4)