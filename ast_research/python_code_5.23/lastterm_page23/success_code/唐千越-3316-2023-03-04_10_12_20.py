fMale=input()
fFemale=input()
fStudents=fMale+fFemale
mratio=eval(fMale)/eval(fStudents)
fratio=eval(fFemale)/eval(fStudents)
sText="The male students ratio is %.2f%.the female students ratio is %.2f%" % (mratio, fratio)
print(sText)
