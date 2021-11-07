n, target = map(int, input().split())
coin = list(int(input()) for _ in range(n))
cnt = 0

for i in range(n-1, -1, -1):
    if target // coin[i] == 0:
        continue
    if target == 0:
        break
    cnt += target // coin[i]
    target = target % coin[i]

print(cnt)