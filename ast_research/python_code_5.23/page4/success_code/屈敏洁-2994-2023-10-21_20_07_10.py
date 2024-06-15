ls = list(eval(input()))
n,m = eval(input())
x = ls[n]
if n<len(ls) and n>=-(len(ls)):
    for i in range(m):
        ls.append(x) 
    print(ls)       
else:
    print("error")    
