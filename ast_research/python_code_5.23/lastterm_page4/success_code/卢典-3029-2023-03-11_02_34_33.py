names=input()
grades=eval(input())
Grades=[grades]
Names=[names]
t=len(Grades)
Ans=[[Names[x],Grades[x]] for x in range(0,t+1)]
print(Ans)
