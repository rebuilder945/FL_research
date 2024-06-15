lst1=input().split(',')
lst2=eval(input())
lst3=list(map(list,zip(lst1,lst2)))
print(lst3)
