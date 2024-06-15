from tkinter.tix import Y_REGION


names = list(input().split(","))
grades = eval(input())
p =[]
for i in range(len(names)):
    x =[names[i],grades[i]]
    p.append(x)
print(p)
