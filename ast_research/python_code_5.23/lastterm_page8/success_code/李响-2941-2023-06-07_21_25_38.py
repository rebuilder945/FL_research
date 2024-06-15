def count_foreign(ids):
    a = [0]
    for x in origin:
       if x[0] == 'L':
          a[0] += 1
    return a[0]

origin=input().split()
print(count_foreign(origin))

