ls = list(eval(input()))
n,m = eval(input())
if n<len(ls) and n>=-(len(ls)):
    for i in range(m):
        ls.append(ls[n]) 
    print(ls)       
else:
    print("error")    
