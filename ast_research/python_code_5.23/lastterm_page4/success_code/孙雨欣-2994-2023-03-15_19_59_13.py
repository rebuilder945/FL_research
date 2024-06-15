ls1=list(eval(input()))
a,b=eval(input())
if a>len(ls1):
    print("error")
else:    
    c=ls1[a]
    for i in range(b):
        ls1.append(c)
    print(ls1)
