a = input().split(",")
b = eval(input())
c = [list(student) for student in list(zip(a, b))]
print(c)
