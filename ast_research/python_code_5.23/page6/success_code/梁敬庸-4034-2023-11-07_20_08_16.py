n=input()
m=input()
color=['red','blue','yellow']
p=['red','blue']
o=['red','yellow']
g=['yellow','blue']
if n==m or n not in color or m not in color:
    print("error")
else:
    if n in p and m in p:
        print("purple")
    elif n in o and m in o:
        print("orange")    
    elif n in g and m in g:
        print("green")    
