arr = [2, 4, 6, 7]
n = 2
result = [0] * n
used = [0] * (len(arr))


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

# per(0)


# def re_per(lev):
#     if lev == n:
#         print(result)
#         return
#     for i in range(len(arr)):
#         result[lev] = arr[i]
#         re_per(lev + 1)

# re_per(0)


# def com(lev, start):
#     if lev == n:
#         print(result)
#         return
#     for i in range(start, len(arr)):
#         result[lev] = arr[i]
#         com(lev + 1, i + 1)


# com(0, 0)


# def subset(lev, ss):
#     if lev == n:
#         if not ss:
#             return
#         print(ss)
#         return
#     subset(lev + 1, ss)
#     subset(lev + 1, ss + [arr[lev]])


# subset(0, [])
