lst = eval(input())
a = "".join(lst)
lst1 = [x for x in a]
lst2 = [chr(ord('a')+x)for x in range(26)]
for x in lst2:
    if x in lst1:
        b = lst1.count(x)
        print(x,",",b)
    else:
        continue




