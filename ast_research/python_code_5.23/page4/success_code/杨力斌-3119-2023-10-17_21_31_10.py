a = eval(input())
numbers = 1,2,3,4,5,6,7,8,9
b = numbers[0:len(a)]
for l in b:
    num1 = a[l]
    if a.count(num1) > 1 and num1 != "Ture":
        num2 = a.count(num1)-1
        for i in range(num2):
            del a[l]
            print(a)
    elif num1 == "Ture":
        pass
print(a)
