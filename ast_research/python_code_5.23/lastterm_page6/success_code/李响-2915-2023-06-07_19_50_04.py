def shuixianhua(s):
  for n in range(100,s+1):  
    a = n//100
    b = (n-100*a)//10
    c = n-100*a-10*b
    if a**3 + b**3 + c**3 == n:
     print(n)
  else:
     print('none')

s = eval(input())
shuixianhua(s)
   
