s=input()
sum=0
if 8<=len(s):
    sum+=1
for i in s:
    if i in "~!@#$%^&*()_=-/,.?<>;:[]{}|\\":
        sum+=1
        break
for i in s:
    if "a"<=i<="z":
        sum+=1
        break
for j in s:
    if "A"<=j<="Z":
        sum+=1
        break
for m in s:
    if "0"<=m <="9":
        sum+=1
        break
print(sum)

