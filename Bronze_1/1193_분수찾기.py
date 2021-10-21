x = int(input())

group = 1

while x > group:
    x -= group
    group += 1

if group % 2 == 0:
    a = x
    b = group - x + 1

else:
    a = group - x + 1
    b = x

print(a, b, sep="/")
