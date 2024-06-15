ls1 = list(eval(input()))
n,m = eval(input())
a = 0
if n>len(ls1)-1 or n<0-len(ls1):
    print("error")
else:
    while True:
        ls1.append(ls1[n])
        a+=1
        if a>m-1:
            break
print(ls1)
    


