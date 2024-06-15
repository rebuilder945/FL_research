str1 = str(input())
num1, num2, num3, num4 = 0, 0, 0, 0
List1 = [chr(y) for y in range(97, 123)]
List2 = [str(z) for z in range(10)]
List3 = [chr(h) for h in range(65, 91)]
for x in str1:
    if x == " ":
        num2 += 1
    elif x in List1 or x in List3:
        num1 += 1
    elif x in List2:
        num3 += 1
    else:
        num4 += 1
print(num1, num2, num3, num4)


