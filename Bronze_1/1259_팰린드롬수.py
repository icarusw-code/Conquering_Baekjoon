def check(s):
    if s == s[::-1]:
        return True
    else:
        return False


while True:
    n = str(input())
    if n == "0":
        break
    if check(n) == True:
        print("yes")
    else:
        print("no")
