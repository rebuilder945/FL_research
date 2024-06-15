a=input()
a=a.split()
b=input()
b=b.split()
a1=int(b[0])
a2=int(b[-1])
if a1 in range(-len(a),len(a)) and a2 in range(-len(a),len(a)):
    a[a1],a[a2]=a[a2],a[a1]    
    print(a)
else:
    print("error")
