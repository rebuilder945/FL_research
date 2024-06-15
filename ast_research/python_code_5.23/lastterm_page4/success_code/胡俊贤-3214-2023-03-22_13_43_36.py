ls=eval(input())
n=ls.count('0')
for i in range(n):
    ls.remove('0')
    ls.append('0')    

