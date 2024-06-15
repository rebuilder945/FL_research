lst = eval(input())
a = max(lst)
b = min(lst)
lst = [i for i in lst if i!=a and i!= b]
print(lst)
