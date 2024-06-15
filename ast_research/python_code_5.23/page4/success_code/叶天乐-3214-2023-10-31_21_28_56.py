ls1 = eval(input())
a = 0
while True:
    ls1.remove(0)
    a+=1
    if ls1.count(0)==0:
        break
for i in range(a):
    ls1.append(0)
print(ls1)



 

       

