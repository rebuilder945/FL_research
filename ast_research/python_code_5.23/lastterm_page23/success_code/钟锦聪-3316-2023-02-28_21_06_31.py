boys = eval(input())
girls = eval(input())
total = boys+girls
iMalestudent = (boys/total)*100
iFemalestudent = (girls/total)*100
sText = "The male students ratio is %.2f %%,the female "\
"students ratio is %.2f %%"%(iMalestudent,iFemalestudent)
print(sText)

