def print_matrix(n):
    m=''
    k=[x+1 for x in range(n)]
    for x in k:
        m=m+str(x)+' '
    t=1
    
    for i in range(n):
        s=str(t)+' '
        a=m[:i*2]+s*(n-i) 
        print(a)
        t+=1

number=eval(input())
print_matrix(number)



