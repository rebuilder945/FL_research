list1 = eval(input())
a,b = eval(input())
if b >= a:
    for i in range(b-a-1):
        list1.pop(a)
    print(list1)
else:
    print("error")
