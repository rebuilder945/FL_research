fMale=input()
fFemale=input()
fStudents=fMale+fFemale
mratio=eval(fMale)/fStudents
fratio=eval(fFemale)/fStudents
sText="The male students ratio is %.2f%,the female students ratio is %.2f%" % (mratio, fratio)
print(sText)
