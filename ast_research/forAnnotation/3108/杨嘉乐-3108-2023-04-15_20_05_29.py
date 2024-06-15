x=eval(input())
for i in range(26):
    alpha=chr(ord('a')+i)
    sum=0
    for m in x:
        for n in m:
            if n==alpha:
                sum+=1
    if sum!=0:
        print(alpha,sum)
