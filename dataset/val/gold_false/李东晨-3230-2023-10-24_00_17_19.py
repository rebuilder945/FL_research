a=eval(input())
a.sort(reverse=True)
for x in a:
    if x !=0:   
        print(x,end="")
    else:
        print("0")
       
