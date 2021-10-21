n = int(input())
target = 1000 - n
money = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in money:
    if target % i == 0:
        cnt += target // i
        break
    else:
        if target % i == i:
            continue
        cnt += target // i
        target = target % i

print(cnt)
