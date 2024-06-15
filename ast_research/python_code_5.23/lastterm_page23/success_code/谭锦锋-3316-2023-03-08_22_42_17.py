male = input()
female = input()
a = eval(male)
b = eval(female)
e = a + b
g = "{:.2f}%".format(a/e*100)
f = "{:.2f}%".format(b/e*100)
print("The male students ratio is",g,", the female students ratio is",f)
