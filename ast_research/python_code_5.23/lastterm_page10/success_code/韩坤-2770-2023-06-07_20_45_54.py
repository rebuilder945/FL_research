n=input()
m=input()
s1=set([])
s2=set([])
dic1={}
dic2={}
for x in n:
    dic1[x]=dic1.get(x,0)+1
for x in m:
    dic2[x]=dic2.get(x,0)+1
s1=set(list(dic1.items()))
s2=set(list(dic2.items()))
if s1==s2:
    print("True")
else:
    print("False")

