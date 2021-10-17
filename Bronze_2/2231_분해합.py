n = int(input())

result = 0

for i in range(1, n + 1):
    tmp = list(map(int, str(i)))
    s = i + sum(tmp)
    if s == n:
        result = i
        break

print(result)
