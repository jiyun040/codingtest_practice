N, M = map(int, input().split())

A = []
for _ in range(N):
    row = input()
    row = row.split()
    row = list(map(int, row))
    A.append(row)

B = []
for _ in range(N):
    row = input()
    row = row.split()
    row = list(map(int, row))
    B.append(row)

result = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(A[i][j] + B[i][j])
    result.append(row)

for row in result:
    print(' '.join(map(str, row)))