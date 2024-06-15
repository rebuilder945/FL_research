n=''.join(eval(input()))
for i in 'abcdefghijklmnopqrstuvwxyz':
    if i in n:
        sum=n.count(i)
        print(i+','+str(sum))
    
    

