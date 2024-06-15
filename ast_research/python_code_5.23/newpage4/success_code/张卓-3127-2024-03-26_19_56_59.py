a = eval(input())
b = [i for i in range(1,a+1,1)]
b.remove(1)
b.append(1)
print(b)
