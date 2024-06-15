a=[i for i in range(1,11,2)]
b=[i for i in range(2,11,2)]
g=[i for i in range(11,19,2)]
h=[i for i in range(12,19,2)]
c=[i for i in range(19,29,2)]
d=[i for i in range(20,29,2)]
e=[i for i in range(29,37,2)]
f=[i for i in range(30,37,2)]
n=eval(input())
if n in a or n in c or n in f or n in h:
    print("red")
elif n in b or n in d or a in e or a in g:
    print("black")
elif n==0:
    print("green")
else:
    print("error")
