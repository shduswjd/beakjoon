N, M = map(int, input().split())

lst = list(range(1, N+1))
# 1 2 3 4 5

for m in range(M):
    i, j = map(int, input().split())
    lst[i-1:j] = reversed(lst[i-1:j])

for i in lst:
    print(i, end= "")