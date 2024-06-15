n = eval(input())
n.sort(reverse=True)
ls=[]
for i in n:
    a = str(i)
    ls.append(a)
str="".join(ls)
print(str)
