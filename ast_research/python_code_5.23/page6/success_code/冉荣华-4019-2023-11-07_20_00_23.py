num=input()
for i in range(num):
    num[i]+=5
    num[i]=num[i]%10
s=num[::-1]
print(s)

