lst=[]
x=0
while True:
    a=input()
    if a=="#":
     break
    a=eval(a)
    lst.append(a)
    x+=1
print(x,sum(lst))


