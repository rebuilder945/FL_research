def print_matrix(n):
    for i in range(n):
        s=[]
        for x in range(n):
            s.append(1)
        for x in range(n):
            if s[x]<i+1:
                s[x]+=x
        for i in s:
            print(i,end=' ')
        print('\n')
      

number=eval(input())
print_matrix(number)



