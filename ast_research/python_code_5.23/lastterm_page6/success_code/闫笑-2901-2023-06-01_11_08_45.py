List1 = []
n = 0
while n >= 0:
    num1 = str(input())
    if num1 == "#":
        break
    else:
        List1.append(num1)
List1 = [int(y) for y in List1]
print(len(List1), sum(List1))
