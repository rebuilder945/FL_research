boy = eval(input())
girl = eval(input())
all = boy + girl 
bc = boy / all * 100
gc = girl / all * 100
# print("The male students ratio is %.2f%%,the female students ratio is 40.00%%"%(bc))
print(f"The male students ratio is {bc:.2f}%,the female students ratio is {gc:.2f}%")

