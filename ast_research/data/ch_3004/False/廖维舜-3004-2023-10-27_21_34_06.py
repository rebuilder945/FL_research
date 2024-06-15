list=eval(input())
lst=[]
for i in range(len(list)):
    n=int(list[i])
    for x in range(2,n):
        if n%x!=0:
            lst.append(n)
        else:
            break
    print(lst)
            

