list = eval(input())
a,b = eval(input())
if a >= len(list):
    print("error")
elif b >= len(list):
    print("error")
else: 
    for i in range(b-a):
        del list[a]
    print(list)
