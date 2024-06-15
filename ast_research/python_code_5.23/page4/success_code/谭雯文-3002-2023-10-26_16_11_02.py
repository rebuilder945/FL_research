ls=eval(input())
b=sum (ls)/len(ls)
if sum(ls)%len(ls)!=0:
    print("%.2f"%b)
else:
    print(int(b))    
