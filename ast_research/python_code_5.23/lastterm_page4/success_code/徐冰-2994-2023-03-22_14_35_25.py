a=list(eval(input()))
n,m=eval(input())
ls=[]
if n>=0 and n in range(0,len(a)) or n<0 and n in range(-len(a),0):
    ls.append(a[n])
    ls1=ls*m
    a.extend(ls1)
    print(a)
else:
    print("error")
