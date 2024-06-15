def count_foreign(ids):
    b=list(ids)
    c=0
    for i in b:
          if len(i)==9:
              c+=1
    return c
         
       

origin=input().split()
print(count_foreign(origin))

