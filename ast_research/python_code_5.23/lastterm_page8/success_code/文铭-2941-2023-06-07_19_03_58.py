def count_foreign(ids):
    js =0
    for x in ids:
         if x[0] in "L":
             js+=1
    return js

origin=input().split()
print(count_foreign(origin))

