ls = list(eval(input()))
n,m = eval(input())

if n<len(ls) and n>=-(len(ls)):
    x = ls[n]
    for i in range(m):
        ls.append(x) 
    print(ls)       
else:
    print("error")    
