x=0
y='0'
n=0
s=0
while y!='#':
    y=input()
    if y!='#':
        x=eval(y)
        n+=1
        s+=x
    else:
        break
print("{} {}".format(n,s))
