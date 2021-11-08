def change(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            a_list[x][y] = 1 - a_list[x][y]

n, m = map(int, input().split())
a_list = [list(map(int, input())) for _ in range(n)]
b_list = [list(map(int, input())) for _ in range(n)]
count = 0

for i in range(n - 2):
    for j in range(m - 2):
        if a_list[i][j] != b_list[i][j]:
            change(i, j)
            count += 1

check = 0
for i in range(n):
    for j in range(m):
        if a_list[i][j] != b_list[i][j]:
            check = 1
            break

if check == 0:
    print(count)
else:
    print(-1)