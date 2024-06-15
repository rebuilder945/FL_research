s = int(input())
lst = [x+1 for x in range(0,s)]
del lst[0]
lst.append(1)
print(lst)
