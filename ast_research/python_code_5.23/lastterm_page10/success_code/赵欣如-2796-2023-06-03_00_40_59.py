s=input()
longeststr=""
a=0
for x in s:
    if ord(x)<48 or  ord(x)>57:
        a+=1
    if a==int(len(s)):
        print("No digits")
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
