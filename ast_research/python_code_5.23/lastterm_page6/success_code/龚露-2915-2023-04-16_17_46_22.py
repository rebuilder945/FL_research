a=eval(input("随便输入一个整数："))
if a < 100:
    print('none')
elif 100<=a<1000:
    for i in range(a+1):
        if len(str(i))==3:        
            x = i%10
            y = i//10%10
            z = i//100
            if x**3+y**3+z**3==i:
                print(i)
else:
    print("153\n370\n371\n407")

