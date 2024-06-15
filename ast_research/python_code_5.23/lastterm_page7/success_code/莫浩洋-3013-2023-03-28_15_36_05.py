# a = 1
# d={}
# n = input()
# while n!="q" :
#     d[n]=d.get(n,0)+1
#     n=input()
# ls = list(d.items() )
# ls.sort(key = lambda x:x[1],reverse=True)
# print("{} {}".format(ls[0][0],ls[0][1]))

# a = list(input().split(" "))
# d={}
# for i in a:
#     d[i]=d.get(i,0)+1
# ls = list(d.items() )
# ls.sort(key = lambda x:x[1],reverse=True)
# max1 = ls[0][1]
# for x in ls:
#     if x[1]==max1:
#         print("{} {}".format(x[0],x[1]))

# ls = list(input().split(" "))
# ls.sort(key = lambda x:ls.count(x),reverse=True)
# print(ls)

# stu = {}
# stu["name"],stu["english"],stu["python"],stu["math"]=list(input().split(" "))
# ls = list(stu.items())
# n = ls.pop(0)
# ls.sort(key=lambda x:int(x[1]),reverse=True)
# stu["avg"]=(int(stu["english"])+int(stu["python"])+int(stu["math"]))/3
# print("%s %.2f %.2f %.2f %.2f"%(n[1],int(ls[0][1]),int(ls[1][1]),int(ls[2][1]),stu["avg"]))

d={}
n = str(input())
while n != "ok":
    ls=list(n.split(" "))
    d[ls[0]]=int(ls[1])
    n=str(input())
print(list(d.keys()))
print(list(d.values()))
if "india" in d:
    print("yes")
else:
    print("no")
a=0
for i in d.values():
    a+=i
print(a)




