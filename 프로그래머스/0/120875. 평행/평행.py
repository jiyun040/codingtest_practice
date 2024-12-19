def solution(dots):
    # 두 점 사이의 기울기를 계산
    def calculate_slope(dot1, dot2):
        return (dot2[1] - dot1[1]) / (dot2[0] - dot1[0])

    # 네 점 중에서 두 점을 선택하여 기울기 비교
    if calculate_slope(dots[0], dots[1]) == calculate_slope(dots[2], dots[3]):
        return 1
    if calculate_slope(dots[0], dots[2]) == calculate_slope(dots[1], dots[3]):
        return 1
    if calculate_slope(dots[0], dots[3]) == calculate_slope(dots[1], dots[2]):
        return 1

    return 0