n = int(input())
arr = list(map(int, input().split()))

result = [0] * n


def r_per(lev):
    if lev == n:
        print(*result)
        return
    for i in range(len(arr)):
        result[lev] = arr[i]
        r_per(lev + 1)


used = [0] * len(arr)


def per(lev):
    if lev == n:
        print(*result)
        return
    for i in range(len(arr)):
        if used[i] == 1:
            continue
        used[i] = 1
        result[lev] = arr[i]
        per(lev + 1)
        used[i] = 0


def com(lev, start):
    if lev == n:
        print(*result)
        return
    for i in range(start, len(arr)):
        result[lev] = arr[i]
        com(lev + 1, i + 1)


# r_per(0)
# per(0)
com(0, 0)
