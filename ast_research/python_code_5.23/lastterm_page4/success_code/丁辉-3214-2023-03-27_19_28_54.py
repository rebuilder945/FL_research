a=eval(input())
for i in range(0,len(a),1):
    if a[i]==0:
        b=a.pop(i)
        c=a+b
        print(c)
