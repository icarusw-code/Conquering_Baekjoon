n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = [0] * 3
card = []


def com(lev, start):
    if lev == 3:
        card.append(result[:])
        return
    for i in range(start, len(arr)):
        result[lev] = arr[i]
        com(lev + 1, i + 1)


com(0, 0)
cnt = []
for i in range(len(card)):
    if sum(card[i]) <= m:
        cnt.append(sum(card[i]))

print(max(cnt))
