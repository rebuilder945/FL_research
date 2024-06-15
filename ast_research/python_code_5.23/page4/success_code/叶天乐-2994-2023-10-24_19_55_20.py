ls1 = list(eval(input()))
n,m = eval(input())
if n >=0 and n <=len(ls1):
       ls1.append(list(ls1[n])*m)
       print(ls1)
else:
    print("error")
