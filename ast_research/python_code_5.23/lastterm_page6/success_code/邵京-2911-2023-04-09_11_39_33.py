a=eval(input())
strnumbers=str(a)
for i in range(0,len(strnumbers)):
    b=int(strnumbers[i])
    d=(b+5)%10
    strnumbers=strnumbers.replace(strnumbers[i],str(d))
codenumbers=strnumbers[::-1]
print(eval(codenumbers))

