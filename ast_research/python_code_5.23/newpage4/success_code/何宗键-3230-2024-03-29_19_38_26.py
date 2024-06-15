a=list(eval(input()))
a.sort(reverse=True)
for i in a:
    if a[0]==0:
     print("0")  
    else:
        print(i,end="") 
