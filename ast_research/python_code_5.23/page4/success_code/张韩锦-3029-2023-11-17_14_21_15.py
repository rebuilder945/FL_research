lst1=input().split(",")
lst2=eval(input())
lst3=[[lst1[i],lst2[i]] for i in range(len(lst1))]
print(lst3)
