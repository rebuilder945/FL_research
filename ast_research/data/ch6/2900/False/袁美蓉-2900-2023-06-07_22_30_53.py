n = eval(input())
if n <= 0 or n != int(n):
    print('illegal input')
if n > 0 and type(n)==int:
    for i in range(2,n):
        count = 0
        for j in range(2,i):
            if i%j == 0:
                count += 1
            continue
        if count == 0:
            s = str(i)
            if s == s[::-1]:
                print(s,end="")


                    




