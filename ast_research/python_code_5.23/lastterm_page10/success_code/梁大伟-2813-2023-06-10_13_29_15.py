s1=input()
s2=input()
t=0
while t!=-1:
    t=s1.find(s2)
    if t==-1:
        break
    s1=s1[0:t]+s1[t+len(s2):]
    print(s1)
