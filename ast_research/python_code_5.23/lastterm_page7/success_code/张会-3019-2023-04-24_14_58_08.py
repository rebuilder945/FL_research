from audioop import avg


s=input().split()
a=s[0]
ls1=[]
for i in range(1,4):
    b=eval(s[i])
    ls1.append(b)
ls=['english','python','math']
m={}
for i in range(3):
    m[ls[i]]=ls1[i]
ls1.sort(reverse=True)
b=ls1[0]
c=ls1[1]
d=ls1[2]
e=(m['english']+m['python']+m['math'])/3
print("%s %.2f %.2f %.2f %.2f"%(a,b,c,d,e))
