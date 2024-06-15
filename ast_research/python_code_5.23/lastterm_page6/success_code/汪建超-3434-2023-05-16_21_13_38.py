a = input()
b = input()
lst = ['red','blue','yellow']
if a not in lst or b not in lst or a ==b:
    print("error")
else:
    if a == 'red' or b == 'red':
        if a== 'blue' or b=='blue':
            print("purple") 
        else:
            print("orange")
    else:
        print("green")
