male=float(input("Enter the number of males: "))
famale=float(input("Enter the number of females: "))
text="The male students ratio is %.2f%%,the female students ratio is %.2f%%" %(male/(male+famale)*100,famale/(male+famale)*100)
print(text)
