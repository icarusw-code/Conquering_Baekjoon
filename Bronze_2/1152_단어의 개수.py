sentence = list(input().split())

count = 0
for i in range(len(sentence)):
    if len(sentence[i]) != 0:
        count += 1

print(count)
