def count_foreign(ids):
    b=[]
    for x in origin:
          if len(x)==9:
              b.append(x)
    c=len(b)
    return c

origin=input().split()
print(count_foreign(origin))

