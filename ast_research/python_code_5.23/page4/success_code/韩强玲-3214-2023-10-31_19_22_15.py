a = eval(input())
b = a.count(0) 
c = [0]*b
for i in a:
    if i == 0:
        a.remove(i)
print(a+c)                                                                                                                                                                                                                                                                                                                                           
