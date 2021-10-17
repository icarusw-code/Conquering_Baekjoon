arr = list(int(input()) for _ in range(9))

print(max(arr))

for i in range(len(arr)):
    if max(arr) == arr[i]:
        print(i + 1)
