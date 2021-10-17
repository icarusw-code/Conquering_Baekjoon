t = int(input())

for _ in range(t):
    arr = list(map(str, input()))
    score = 0
    cnt = 1
    for i in range(len(arr)):
        if arr[i] == "O":
            score += cnt
            cnt += 1
        else:
            cnt = 1

    print(score)
