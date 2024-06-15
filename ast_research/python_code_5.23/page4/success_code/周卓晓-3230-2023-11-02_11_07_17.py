n = eval(input())
n.sort(reverse=True)
ls=[]
if n[0]!=0:
    for i in n:
        a = str(i)
        ls.append(a)
    str="".join(ls)
    print(str)
else:
    print("0")
    



