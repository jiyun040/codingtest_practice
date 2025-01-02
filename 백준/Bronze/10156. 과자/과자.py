K, N, M = map(int, input().split())
answer = K * N
need = answer - M
print(max(0, need))