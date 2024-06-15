def count(lst,n):
    ceng=0
    while ceng<n:
        for i in range(len(lst)):
            if type(lst[i])==type([]):
                ceng+=1
                lst=lst[i]
            break
    return len(lst)
lst=eval(input())
n=eval(input())
a=count(lst,n)
print(a)
    

