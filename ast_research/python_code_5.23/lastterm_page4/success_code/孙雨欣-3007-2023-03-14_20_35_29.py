ls1=eval(input())
a,b=eval(input())
if a<len(ls1) and b<(len(ls1)):
    if a<b:
        del ls1[a:b]
        print(ls1)
    else:
        del ls1[b+1:a+1]
        print(ls1)
else:
    print("error")
        
    
