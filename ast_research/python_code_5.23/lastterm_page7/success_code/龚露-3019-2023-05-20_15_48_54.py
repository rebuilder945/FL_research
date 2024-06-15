ls = input().split()
k,v,l,m=ls
di=(('name',k),('english',eval(v)),('python',eval(l)),('math',eval(m)))
stu=dict(di)
ls1=[eval(v),eval(l),eval(m)]
ls1.sort(reverse=True)
s = sum(ls1)
n = len(ls1)
final=s/n
stu['avg']=final
print("%s,%.2f,%.2f,%。2f,%.2f"% k,ls1[0],ls1[1],ls1[2],final)

