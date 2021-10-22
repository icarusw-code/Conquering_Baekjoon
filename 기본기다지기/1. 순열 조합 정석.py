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


# 부분집합
def subset(lev, ss):
    if lev == n:
        if not ss:  # 공집합은 제거
            return
        print(ss)
        return
    subset(lev + 1, ss + [arr[lev]])  # 해당 원소를 선택 O => [] + [1] = [1]
    subset(lev + 1, ss)  # 해당 원소를 선택 X

# 다음 순열


array = list(map(int, input().split()))


def next_perm(array):
    i = len(array) - 1
    while i > 0 and array[i-1] >= array[i]:
        i -= 1

    if i <= 0:
        return False

    j = len(array) - 1
    while array[i-1] >= array[j]:
        j -= 1

    array[i-1], array[j] = array[j], array[i-1]

    j = len(array) - 1
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

    return True


if next_perm(array):
    print(array)






# r_per(0)
# per(0)
# com(0, 0)
# subset(0, [])
