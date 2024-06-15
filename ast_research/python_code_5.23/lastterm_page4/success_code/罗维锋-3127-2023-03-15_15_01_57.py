n=eval(input())
a=[value for value in range(1,n+1)]
for x in range(1):
    a.insert(len(a),a[0])
    del a[0]
print(a)

