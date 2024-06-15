n=eval(input())
p=[]
for x in range(100,n+1):
    if x==int(str(x)[0])**3+int(str(x)[1])**3+int(str(x)[2])**3:
        p.append(x)
        print(x)
    elif p==[]:
        print('none')
    
