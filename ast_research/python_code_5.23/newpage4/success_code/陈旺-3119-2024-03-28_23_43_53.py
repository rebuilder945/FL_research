a=input()
if a==("[]"):
   print("[]")
else:
    a=a.strip("[")
    a=a.rstrip("]")
    b=[eval(q) for q in a.split(",")]
    b.reverse()#reverse函数的使用
    p=[]
    for el in b:
        if int(p.count(el))<1:
            p.append(el)
    p.reverse()
    print(p) 
