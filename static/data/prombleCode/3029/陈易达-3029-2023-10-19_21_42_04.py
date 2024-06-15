# # n,m,l = eval(input())
# # ls = [n+i*l for i in range(m)]
# # print(ls)
#
# l = eval(input())
# n,m = eval(input())
# if n > len(l)-1 or m > len(l)-1:
#     print("error")
# else:
#     if n <= m:
#         del l[n:m]
#     else:
#         del l[n:m:-1]
#     print(l)


names = list(input().split(','))
scores = list(input().strip('[]').split(','))
a = list(zip(names,scores))
students = []
for x,y in a:
    student = [x,int(y)]
    students.append(student)
print(students)
