a=input() or '#'
sum=0
amount=0
while a!='#':
    sum=sum+eval(a)
    amount=amount+1
    a=input() or '#'
print(amount,sum)
