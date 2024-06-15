lst=eval(input())
str=''.join(lst)
for x in 'abcdefghijklmnopqrstuvwxyz':
    if x in str:
        y=str.count(x)
        temp=x+','+str(y)
print(temp)

