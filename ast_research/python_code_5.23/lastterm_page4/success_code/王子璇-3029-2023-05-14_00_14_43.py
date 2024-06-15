name=input().split(",")
grade=eval(input())
lst=[[name[i],grade[i]] for i in range(len(name))]
print(lst)
