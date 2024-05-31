# 세로 읽기

# 행렬 입력
mat = [list(map(str, input())) for _ in range(5)]

# 행렬에서 가장 긴 리스트
max_len = 0
for i in range(5):
    if len(mat[i]) > max_len:
        max_len = len(mat[i])

# 없는 값은 공백으로 채우자
for i in range(5):
    if len(mat[i]) < max_len:
        mat[i].extend([0] * (max_len - len(mat[i])))


for col in range(max_len):
    for row in range(5):
        x = mat[row][col]
        if x == 0:
            continue
        else:
            print(x, end="")
