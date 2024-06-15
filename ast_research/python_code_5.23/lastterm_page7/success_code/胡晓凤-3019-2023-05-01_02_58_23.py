a,b,c,d=input().split(" ")
# print(a,b,c,d)
stu={("name","a"),("english","b"),("python","c"),("math","d")}
avg=(int(b)+int(c)+int(d))/3
avg=("%.2f")%avg
b=eval(b)
c=eval(c)
d=eval(d)
b=("%.2f")%b
c=("%.2f")%c
d=("%.2f")%d
if eval(b)>=eval(c):
    if eval(c)>=eval(d):
        print(a,b,c,d,avg)
    else:
        if eval(b)>=eval(d):
            print(a,b,d,c,avg)
        else:
            print(a,d,b,c,avg)
elif eval(c)>=eval(b):
    if eval(b)>=eval(d):
        print(a,c,b,d,avg)
    else:
        if eval(c)>=eval(d):
            print(a,c,d,b,avg)
        else:
            print(a,d,c,b,avg)
# # list1=[b,c,d]
# # list1.sort(reverse=True)
# # m=map(str,list1)
# # n=" ".join(m)
# print(a,n,avg)

