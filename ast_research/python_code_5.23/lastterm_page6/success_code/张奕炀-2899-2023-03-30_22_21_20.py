number1,number2 = input().split()               #间隔空格在一行输入参数
number1 = eval(number1)
number2 = eval(number2)
list0 = []
if (number2 - number1 < 3) or (number2 > 10) or (number1 < 0):
    print("illegal input")
else:
    for i in range(number2 - number1):
        number = number1 + i
        list0.append(number)
list1 = []
for i in range(len(list0)):
    for j in range(len(list0)):
        for k in range(len(list0)):
            if i != j and j != k and i != k:
                answer = ([list0[i],list0[j],list0[k]])
                answer = "".join(map(str,answer))
                list1.append(answer)
list1 = list(map(int,list1))            #map函数返回不是列表，需要在前面加list()
for i in range(len(list1)-1,-1,-1):
    if list1[i] <= 100:
        list1.pop(i)
list1 = list(map(str,list1))
last = " ".join(list1)
print(last)
