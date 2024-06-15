def count_foreign(ids):
    people=0
    for x in origin:
        if 'L'  in x:
            people+=1
    return people
       
        

origin=input().split()
print(count_foreign(origin))

