def count_foreign(ids):
    a = 0
    for x in ids:
         if "L"  in x:
             a = a+1
    return a

origin=input().split()
print(count_foreign(origin))

