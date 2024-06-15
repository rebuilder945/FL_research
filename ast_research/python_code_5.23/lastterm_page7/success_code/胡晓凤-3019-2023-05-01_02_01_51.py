a,b,c,d=input().split(" ")
stu={("name","a"),("english","b"),("python","c"),("math","d")}
avg=sum(int(b)+int(c)+int(d))
avg=("%.2f")%avg
b,c,d=("%.2f","%.2f","%.2f")%b,c,d
list1=[b,c,d]
list1.sort(reverse=True)
b=map(str,list1)
c=" ".join(b)
print(a,c,avg)

