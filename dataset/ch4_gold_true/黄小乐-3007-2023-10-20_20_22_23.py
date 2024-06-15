lst = list(eval(input()))
x,y = input().split(",")
x = int(x)
y = int(y)
b = len(lst)
if x>b-1 or y>b-1 or x>y:
    print("error")
else:
    del lst[x:y]
    print(lst)
    
