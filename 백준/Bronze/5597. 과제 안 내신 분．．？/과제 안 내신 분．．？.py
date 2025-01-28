students = set(range(1, 31))

for _ in range(28):
    n = int(input())
    students.remove(n)

missing_students = sorted(students)
print(missing_students[0])
print(missing_students[1])