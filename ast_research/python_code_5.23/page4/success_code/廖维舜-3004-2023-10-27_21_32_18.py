list=eval(input())
lst=[]
for i in range(len(list)):
    n=int(list[i])
    for x in range(2,n):
        if n%x==0:
            break
        else:
            lst.append(n)
    print(lst)
            

