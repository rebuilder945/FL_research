male = eval(input())
female = eval(input())
male = (male/(male+female))*100
female = 100-male
print("The male students ratio is %.2f%%,the female students ratio is %.2f%%"%(male,female))

