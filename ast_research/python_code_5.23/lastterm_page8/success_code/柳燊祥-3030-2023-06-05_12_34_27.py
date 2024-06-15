names=input().split(",")
grades=eval(input())
t=[[names[i],grades[i]] for i in range(len(grades))]
sorted(t,key=lambda x:x[1],reverse=True)
print(t)


