a=0   #数值
b=0   #个数
c=0   #累积
d='1'
while d!='#':
    d=input()
    if d!='#':
        a=eval(d)
    b+=1
    c+=a
print("{} {}".format(b-1,c-a))
