a = eval(input())
b = eval(input())
a = a / (a + b)
b = 1 - a
print("The male students ratio is %.2f%% , the female students ratio is %.2f%%."%(100*a,100*b))
