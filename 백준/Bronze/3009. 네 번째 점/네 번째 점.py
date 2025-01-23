x_axis = []
y_axis = []

for i in range(3):
    x, y = map(int, input().split())
    #현재 입력받은 값이 존재한다면 지우고
    #존재하지 않는다면 추가함
    #-> 네 점 중 두 점은 같은 좌표를 가지니까 두 번 등장한 것은 지워지고 한 번 등장한 것은 남게 되어서 출력하게 되는 것
    if x in x_axis:
        x_axis.remove(x)
    else:
        x_axis.append(x)
    if y in y_axis:
        y_axis.remove(y)
    else:
        y_axis.append(y)

print(*x_axis, *y_axis)