n = input()
list1 = [1+x for x in range(0,int(n))]
a = list1.pop(0)
list1.append(a)
print(list1)
