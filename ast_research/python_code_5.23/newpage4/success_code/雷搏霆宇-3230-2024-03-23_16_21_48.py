s = list(eval(input()))

 # print(s)
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i] < s[j]:
            s[i],s[j]=s[j],s[i]
for t in s:
    print(t,end="")

    

