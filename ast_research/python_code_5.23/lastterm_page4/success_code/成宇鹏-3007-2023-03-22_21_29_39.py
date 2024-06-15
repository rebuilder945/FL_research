ls = input().split(",")
n,m = eval(input())
a = [x for x in range(len(ls))]
for i in range(len(ls)):
    if n not in a  or m not in a :
        print("error")
    else:
        if n <= m :
            if i >= n and i < m: 
                print(ls.pop(i))
                
            else:
                continue
        else:
            continue
