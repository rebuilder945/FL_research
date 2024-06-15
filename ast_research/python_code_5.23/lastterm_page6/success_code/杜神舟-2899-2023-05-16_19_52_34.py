n,m=input().split()
list1=[]
if int(m)-int(n)<=2 or int(m)<0 or int(n)<0 :
    print('illegal input')
else:
    for x in range(100,100*int(m)):
        for y in range(3):
            if int(str(x)[y])>=int(m) or int(str(x)[y])<int(n):
                break
        else:
            if str(x)[0]==str(x)[1] or str(x)[0]==str(x)[2] or str(x)[2]==str(x)[1]:
                pass
            else:
                list1.append(str(x))
if list1==[]:
    print('illegal input')
else:
    print(' '.join(list1))
