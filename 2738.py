n, m = map(int, input().split())

# 행렬 a
mat_a = []
for i in range(n):
    row = list(map(int , input().split()))
    mat_a.append(row)
    

# 행렬 b입력과 동시에 계산
ans = []
for i in range(n):
    lst = []
    row = list(map(int, input().split())) # 3 3 3 
    for j in range(m):
        # 입력받기
        x = row[j]
        lst.append(x + mat_a[i][j])
    ans.append(lst)

for i in range(n):
    for j in range(m):
        print(ans[i][j], end=" ")
    print()



