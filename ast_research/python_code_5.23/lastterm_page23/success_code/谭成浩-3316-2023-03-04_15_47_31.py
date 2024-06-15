smale=eval(input())
sfemale=eval(input())
s1=smale/(smale+sfemale)*100
s2=sfemale/(smale+sfemale)*100
print('The male students ratio is {:.2f}%,the female students ratio is {:.2f}%'.format(s1,s2))
