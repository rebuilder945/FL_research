list = eval(input())
for num in list:
    if list.count(num) == 1:
        print(num)
    else:
        print(False)
