a=input()
for i in range(0,len(a)):
    b=int(a[i])
    d=(b+5)%10
    a=a.replace(a[i],str(d),1)
codenumbers=a[::-1]
print(codenumbers)

