ls=[]
a=0
while True :
    b=input()
    if b!='#':
        ls.append(eval(b))
        a=a+1
    else:
        break
print(a,sum(ls))

