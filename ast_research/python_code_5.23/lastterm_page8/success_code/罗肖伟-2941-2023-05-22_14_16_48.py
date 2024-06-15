def count_foreign(ids):
    number1=[x for x in  ids]
    s=0
    for x in number1:
        if x[0]=="L":
            s+=1
    return s
            
          


origin=input().split()
print(count_foreign(origin))

