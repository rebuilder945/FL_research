male=eval(input())
female=eval(input())
total=male+female
male="{:.2%}".format(male/total)
female="{:.2%}".format(female/total)
print("The male students ratio is %s,the female students ratio is %s"%(male,female))
