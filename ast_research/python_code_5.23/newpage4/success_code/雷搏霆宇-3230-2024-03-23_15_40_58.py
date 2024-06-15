s = list(eval(input()))
Max =[]
 # print(s)
k = 0
for i in s: 
    if i > k:
        k = i 
        Max.insert(0,k)
    elif i < k:
        k = i
        Max.insert(1,k)
print(Max)
for t in Max:
    print(t,end="")

    

