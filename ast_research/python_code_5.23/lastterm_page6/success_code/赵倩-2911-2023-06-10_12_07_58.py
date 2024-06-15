a=list(input())
l=[]
s=[]
for i in a:
    l.append(int(i))
for i in l:
    i=(i+5)%10
    s.append(i)
for i in range(len(s)//2):
    s[i],s[len(s)-1-i]=s[len(s)-1-i],s[i]
print("".join(str(x) for x in s))









