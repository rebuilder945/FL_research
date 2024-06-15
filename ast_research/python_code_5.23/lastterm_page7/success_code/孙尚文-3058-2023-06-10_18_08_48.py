while True:
    b={}
    a=input()
    if a=="q":
        break
    else:
        b[eval(a)]=b.get(eval(a),0)+1
lst=[]
for k,v in b.items():
    lst.append([k,v])
    lst.sort(kay=lambda x:x[1],reverse=True)
lst2=[]
lst2.append(lst[0][0])
lst2.append(lst[0][1])
print(" ".join(map(str,lst2)))



