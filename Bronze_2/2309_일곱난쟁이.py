arr = [int(input()) for _ in range(9)]
tmp = [0] * 7
result = []


def com(lev, start):
    if lev == 7:
        result.append(tmp[:])
        return
    for i in range(start, 9):
        tmp[lev] = arr[i]
        com(lev + 1, i + 1)


com(0, 0)

for i in result:
    if sum(i) == 100:
        i.sort()
        for j in i:
            print(j)
        break
