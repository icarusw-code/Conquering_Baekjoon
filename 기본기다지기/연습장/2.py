n = 2
arr = [2, 4, 6, 7]
path = [0] * n

used = [0] * len(arr)


def per(lev):
    if lev == n:
        print(*path)
        return
    for i in range(len(arr)):
        if used[i] == 1:
            continue
        path[lev] = arr[i]
        used[i] = 1
        per(lev + 1)
        used[i] = 0


def re_per(lev):
    if lev == n:
        print(*path)
        return
    for i in range(len(arr)):
        path[lev] = arr[i]
        re_per(lev + 1)


def com(lev, start):
    if lev == n:
        print(*path)
        return
    for i in range(start, len(arr)):
        path[lev] = arr[i]
        com(lev + 1, i + 1)


per(0)
print("==============================")
re_per(0)
print("==============================")
com(0, 0)
