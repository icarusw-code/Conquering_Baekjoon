n = int(input())
cost = list(map(int, input().split()))
cost.sort()
time = []

for i in range(len(cost)):
    time.append(sum(cost[:i+1]))

print(sum(time))