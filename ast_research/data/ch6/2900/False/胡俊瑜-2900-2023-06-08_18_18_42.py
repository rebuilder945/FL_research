from math import sqrt #平方根函数,返回一个函数的正平方根
def P(x): #判断是否为素数
    f = True
    i = 2
    while i <= sqrt(x):
        if x % i == 0:
            f = False
        i = i+1 
    return f
def Q(x): #判断是否为回文数
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False
n =eval(input())
finlist=[]
m=2
while m<n:
	if P(m) == True and Q(m) == True:	
		finlist.append(m)
	m+=1
print(*finlist)


  
if n<0 or isinstance(n,float)==True:
	print("illegal input")


