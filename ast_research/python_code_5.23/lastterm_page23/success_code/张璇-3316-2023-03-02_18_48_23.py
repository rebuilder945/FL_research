man = eval(input())
woman = eval(input())
start = "The male students ratio is"
fina = "the female students ratio is"
a = man/(man+woman)*100
b = woman/(man+woman)*100
print("%s %.2f%%,%s %.2f%%"%(start,a,fina,b))
