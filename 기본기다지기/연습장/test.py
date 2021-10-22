from itertools import combinations

arr = [2, 4, 6, 7]
result = []

for i in combinations(arr, 2):
    result.append(list(i))

print(result[0])
