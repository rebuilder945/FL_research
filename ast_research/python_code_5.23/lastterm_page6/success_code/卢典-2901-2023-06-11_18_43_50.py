lis=[]
n=input()
while n!='#':
    lis.append(eval(n))
    n=input()
print(len(lis),sum(lis))
