search=eval(input())
out=[] 
for i in search:
    if search.count(i) is int(1):
        out.append(i)

if len(out)==0:
    print("False")  
else:    
    out.sort(reverse=True)
    out.reverse()
    print(eval(out))

