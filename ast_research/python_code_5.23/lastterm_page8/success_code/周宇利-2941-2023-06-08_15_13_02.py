def count_foreign(ids):
    list1=list(ids)
    for i in list1:
         a=list(i)
         b=0
         if a[1]=='L':
             b+=1
    return b


origin=input().split()
print(count_foreign(origin))

