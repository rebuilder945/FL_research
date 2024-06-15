s='aabcdefaabbccdeffffffffffff'
 
c={}
 
for i in s:
 
if i not in c.keys():
 
c[i]=0
 
if i in c.keys():
 
c[i]=c[i]+1
 
h=0
 
for k in c.keys():
 
if h<c[k]:
 
h=c[k]
 
o=k
 
print h,o
