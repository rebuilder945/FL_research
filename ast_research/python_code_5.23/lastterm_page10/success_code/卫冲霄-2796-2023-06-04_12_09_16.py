s=input()
sum = 0
for m in s:
    if "0" <= m <= "9":
        sum += 1
if sum == 0:
    print("No digits")
else:
    ls=[0 for x in range(len(s))]
    for i in range(1,len(s)+1):
        if "0" <=s(i-1) <="9":
            ls[i]=ls[i-1]+1
    for j in range(len(ls)-1,-1,-1):
        if ls[j]==max(ls):
            print(s[j-max(ls):j+1])
            break


