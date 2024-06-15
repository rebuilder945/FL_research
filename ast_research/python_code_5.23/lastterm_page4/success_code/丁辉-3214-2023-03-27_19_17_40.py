a=eval(input())
for i in range(0,len(a),1):
    if a[i]==0:
        b=a.pop(a[i])
        c=b+a[i]
        print(c)
