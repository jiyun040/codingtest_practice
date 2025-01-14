H, M = map(int, input().split())
C = int(input())

M += C

# 분을 시간으로 변환
H += M // 60
M %= 60

# 시간을 24시간 형식으로 변환
H %= 24

print(H, M)