lst=eval(input())
for i in lst[:]:
    if i >=1:
        for x in range(2,i//2+1):
            if i % x ==0:
                lst.remove(i)
                break
        print(lst)
        

