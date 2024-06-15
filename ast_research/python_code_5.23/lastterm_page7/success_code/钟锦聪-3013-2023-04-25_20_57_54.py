item  =  input() 
numbers  =  {}
while item  != "ok":
    num = item.split()
    country = num[0]
    number = num[1]
    numbers[country] = number
    item  =  input()
c = []
d = numbers.keys()
for x in d:
    c.append(x)
a = []
b = numbers.values()
for x in b:
    a.append(int(x))
print(c)
print(a)
if "India" in c:
    print("yes")
else:
    print("no")
print(sum(a))
