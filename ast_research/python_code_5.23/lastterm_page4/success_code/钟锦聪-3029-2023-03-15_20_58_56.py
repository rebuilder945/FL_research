names = input()
namess = names.split(',')
ages = eval(input())
b=len(namess)
c=[]
for i in range(b-1):
    x = namess[i] 
    y = ages [i] 
    a = [x,y]
    c.append(a)
print(c)
