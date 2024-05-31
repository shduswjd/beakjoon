# 행렬 입력
mat = [list(map(int, input().split())) for _ in range(9)]

max_num = mat[0][0]
row, col = 0, 0
for i in range(9):
    for j in range(9):
        if max_num < mat[i][j]:
            max_num = mat[i][j]
            row = i
            col = j
print(max_num)
print(row+1, col+1)

