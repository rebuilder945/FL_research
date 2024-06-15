names=input().split(",")
grades=eval(input())
t=[[names[i],grades[i]] for i in range(len(grades))]
t.sort(key=lambda x:x[1])
print(t)


