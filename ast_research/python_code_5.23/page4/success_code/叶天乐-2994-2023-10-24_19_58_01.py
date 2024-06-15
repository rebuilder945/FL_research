ls1 = list(eval(input()))
n,m = eval(input())
if n>len(ls1)-1:
       ls1.append(ls1[n])
       print(ls1)
else:
    print("error")
