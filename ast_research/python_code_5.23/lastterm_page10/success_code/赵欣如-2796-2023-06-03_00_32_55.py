s=input()
longeststr=""
for i in range(len(s)):
    if s[i].isdecimal():
        num=s[i]
        j=i+1
        while j<len(s) and s[j].isdecimal():
            num+=s[j]
            j+=1
        if len(num)>=len(longeststr):
            longeststr=num
print(longeststr)
