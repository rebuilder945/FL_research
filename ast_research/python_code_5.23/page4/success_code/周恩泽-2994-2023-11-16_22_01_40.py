n1=list(eval(input()))
n2,n3=eval(input())
if (n2>=0 and n2<(len(n1)-1)) or (n2<0 and abs(n2)<len(n1)):
    for x  in range(n3):
        n1.append(n1[n2])
    print(n1)
else:
    print("error")


        

