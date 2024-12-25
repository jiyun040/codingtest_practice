K = int(input())  # 반의 수 입력
for i in range(1, K + 1):
    data = list(map(int, input().split()))  # 학생 수와 성적을 리스트 형태로 입력
    N = data[0]  # 학생 수
    math = data[1:]  # 점수 리스트

    max_math = max(math)  # 최대 점수
    min_math = min(math)  # 최소 점수
    math.sort(reverse=True)  # 점수 내림차순 정렬
    gap = max(math[j] - math[j + 1] for j in range(N - 1))  # 가장 큰 점수 차이

    print(f"Class {i}")
    print(f"Max {max_math}, Min {min_math}, Largest gap {gap}")