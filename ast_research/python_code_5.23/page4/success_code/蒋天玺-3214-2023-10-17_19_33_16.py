a = eval(input())
quantity = a.count(0)
for i in range(quantity):
    a.remove(0)
for i in range(quantity):
    a.append(0)
print(a)




