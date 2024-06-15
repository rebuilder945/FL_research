n=input()
m=input()
p=['red','blue']
o=['red','yellow']
g=['yellow','blue']
if n==m:
    print("error")
else:
    if n in p and m in p:
        print("purple")
    elif n in o and m in o:
        print("orange")    
    elif n in g and m in g:
        print("green")    
