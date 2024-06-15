a=eval(input())
ii=[]
ss=""
for i in a:
    if a.count(i)==1:
        ii.append(i)
if ii==[]:
    print("False")
else:
    ii.sort()
    for x in ii:
        y=str(x)
        y=y+","
        ss=ss+y
    #print(ss)1,4,5,这个时候只需要去掉（字符串的切片）最后的逗号就好了
    ss=ss[:-1]
    print(ss)
    

