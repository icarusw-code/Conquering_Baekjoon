arr = []
result = []
for _ in range(10):
    arr.append(int(input()))

for i in range(10):
    result.append(arr[i] % 42)

print(len(set(result)))
