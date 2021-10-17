a = int(input())
b = int(input())
c = int(input())

solve = a * b * c
# ans = [0] * 10

# for i in str(solve):
#     ans[int(i)] += 1

# for i in ans:
#     print(i)

for i in range(10):
    print(str(solve).count(str(i)))
