a = eval(input())
for num1 in a:
    if a.count(num1) > 1 and num1 != "Ture":
        num2 = a.count(num1)-1
        for i in range(num2):
            del a[num1]
    elif num1 == "Ture":
        pass
print(a)
