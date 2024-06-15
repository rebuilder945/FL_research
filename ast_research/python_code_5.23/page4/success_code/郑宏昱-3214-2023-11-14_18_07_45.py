a = eval(input())  
b = a.count(0)  
a = [i for i in a if i != 0]  
a.extend([0]*b)  
print(a)

