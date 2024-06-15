names=input().split(",")
grades=eval(input())
t=[[names[i],grades[i]] for i in range(len(grades))]
tSorted=t.sort(grades)
print(tSorted)


