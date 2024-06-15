names=input().split(",")
Grades=eval(input())
t=len(Grades)
Ans=[[names[x],Grades[x]] for x in range(0,t)]
print(Ans)
