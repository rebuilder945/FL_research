a=list(eval(input()))
b=[]
for i in a:
    x=(i+5)%10
    b.append(x)
b.reverse()
for j in b:
    print(j,end="") 
