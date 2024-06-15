# class student:
#     def __init__(self,name,age,score):
#         self.name=name
#         self.age=int(age)
#         self.score=int(score)
#     def get_naem(self):
#         return str(self.name)
# s=input().split()
# print(''.join(s))
# import copy
# a=eval(input())
# b=copy.deepcopy(a)
# a[0]=b[-2]
# a[1]=b[-1]
# for i in range(2,len(a)):
#     a[i]=b[i-2]
# a.reverse()
# print(a)
n=input().split(',')
s=eval(input())
ls=[]
for i in range(len(s)):
    ls.append([n[i],s[i]])
print(ls)
# tom,jack,jone,mike

# [88,89,34,90]


