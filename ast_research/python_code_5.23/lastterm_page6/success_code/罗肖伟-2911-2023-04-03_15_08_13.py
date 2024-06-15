a=eval(input())
s=str(a)
for i in range(len(s)):
    s1=int(s[i])
    s1+=5
    s1=s1%10
    s1=str(s1)
    s=s.replace(s[i],s1)
s=s[::-1]
print(s)   
