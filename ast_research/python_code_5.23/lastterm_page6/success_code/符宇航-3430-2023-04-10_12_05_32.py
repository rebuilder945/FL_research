n = eval(input())
if n>2 and n<=5:
    ss='spring'
if n>5 and n<=8:
    ss='summer'
if n>8 and n<=11:
    ss='autumn'
if n>0 and n<=2 or n==12:
    ss='winter'
if n>12 and n<=0:
    ss='error'

print(ss)

