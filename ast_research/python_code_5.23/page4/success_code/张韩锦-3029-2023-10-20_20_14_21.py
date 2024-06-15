name=input().split(",")
score=eval(input())
lst=[[name[i],score[i]] for i in range(len(name))]
print(lst)

