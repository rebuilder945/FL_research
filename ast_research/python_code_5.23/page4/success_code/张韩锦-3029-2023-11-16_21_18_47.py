lst1=input().split(",")
lst2=eval(input())
lst3=[ [x,y]for x in lst1 for y in lst2]
print(lst3)
