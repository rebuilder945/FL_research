a=input()
score=eval(input())
name=a.split(",")
lst=[[name[i],score[i]] for i in range(len(score))]
print(lst)
