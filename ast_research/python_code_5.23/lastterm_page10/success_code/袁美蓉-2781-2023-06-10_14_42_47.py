a = input()
a.split()
b =[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2,0]
if len(a)!=18:
    print("Error")
elif len(a)==18:
    for i in range(len(a)):
        for j in(range(len(b))):
            i = j
            n=a[i]*b[i]
            n+=n
            m=(12-n)%11
            if m==a[-1]:
                print('Correct')
            else:
                print('Wrong')

