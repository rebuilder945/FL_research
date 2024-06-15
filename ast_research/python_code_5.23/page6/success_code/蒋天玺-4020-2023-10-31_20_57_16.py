h = eval(input())
n = eval(input())
#1 10   2th s+10*0.5**(n-1)*2  3th s+10*0.5**(n-1)*2
s = 0
for i in range(1,n+1):
    s = s+10*0.5**(i-1)*2
print(s-10)
