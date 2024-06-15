a=eval(input())
s=[]
for i in range (len(a)):
    if a.count(a[i])==1:
       s.append(a[i])

    #print(s[x],end=",")这种情况输出的末尾也会有一个逗号。
if len(s)>0:
    s.sort()
    s=",".join(str(i)for i in s)
    print(s)
if len(s)==0:
    print("False")
