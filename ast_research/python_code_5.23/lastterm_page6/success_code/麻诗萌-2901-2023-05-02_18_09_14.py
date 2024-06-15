n=input()or'#'
s=0
m=0
while n!="#" :
    s=s+int(n)
    m+=1
    n=input()or'#'
print(m,s)
