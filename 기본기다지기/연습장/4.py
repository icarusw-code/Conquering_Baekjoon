# n = int(input())
arr = [2, 4, 6, 7]
# result = [0] * n

# used = [0] * len(arr)


# def per(lev):
#     if lev == n:
#         print(result)
#         return
#     for i in range(len(arr)):
#         if used[i] == 1:
#             continue
#         result[lev] = arr[i]
#         used[i] = 1
#         per(lev + 1)
#         used[i] = 0


# def com(lev, start):
#     if lev == n:
#         print(result)
#         return
#     for i in range(start, len(arr)):
#         result[lev] = arr[i]
#         com(lev + 1, i + 1)


# def r_per(lev):
#     if lev == n:
#         print(result)
#         return
#     for i in range(len(arr)):
#         result[lev] = arr[i]
#         r_per(lev + 1)


# per(0)
# print("=====================")
# com(0, 0)
# print("=====================")
# r_per(0)
# print("=====================")


# def subset(lev, ss):
#     if lev == n:
#         if not ss:
#             return
#         print(ss)
#         return
#     subset(lev + 1, ss + [arr[lev]])
#     subset(lev + 1, ss)


# subset(0, [])


def next_perm(arr):
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1

    if i <= 0:
        return False

    j = len(arr) - 1
    while j > 0 and arr[j - 1] >= arr[j]:
        j -= 1

    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return True


if next_perm(arr):
    print(arr)
