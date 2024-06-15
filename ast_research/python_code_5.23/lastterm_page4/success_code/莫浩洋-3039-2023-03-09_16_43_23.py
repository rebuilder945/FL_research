a=list(eval(input()))
ma=max(a)
mi=min(a)
num_a=a.count(ma)
num_b=a.count(mi)
for i in range(0,num_a):
    a.remove(ma)
for i in range(0,num_b):
    a.remove(mi)
print(a)
