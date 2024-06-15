a=input() 
s1={}
while(a!="q"):
    s1[a]=s1.get(a,0)+1
    a=input() 
s2=[]
for f,v in s1.items():
    s2.append([f,v])
s2.sort(key=lambda x:x[1], reverse=True)
print(s2[0][0],s2[0][1])
