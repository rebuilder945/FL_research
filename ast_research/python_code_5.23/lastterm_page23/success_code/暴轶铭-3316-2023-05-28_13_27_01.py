male = eval(input())
female = eval(input())
malerate = (male / (male + female))*100
femalerate = (female / (male + female))*100
print("The male students ratio is %.2f%,the female students ratio is %.2f%"%(malerate,femalerate))
