a=eval(input())
for i in range(0,len(a),1):
    if a[i]==0:
        a.remove(a[i])
        b=a+[0]
        print(b)
