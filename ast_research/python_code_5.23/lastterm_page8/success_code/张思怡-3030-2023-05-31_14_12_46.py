a=input().split(',')
b=input().split(",")
d=[]
# print(a,b,type(a),type(b))
for i in range (len(a)):
    # ci.append(a[i])
    ci=[a[i],eval(b[i])]
    d.append(ci)
d.sort(key=lambda x:x[1])
print(d)
