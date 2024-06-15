lst = list(eval(input()))
x,y = input().split(",")
x = int(x)
y = int(y)
b = len(lst)
ls2 = []
if x>b-1 or y>b-1 or x>y:
    print("error")
else:
    for i in range(x,y):
        lst.pop(i)
        ls2 = lst
    print(ls2)
    
