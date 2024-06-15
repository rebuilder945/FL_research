fMale=eval(input())
fFemale=eval(input())
fStudents=fMale+fFemale
mratio=fMale/fStudents
fratio=fFemale/fStudents
sText="The male students ratio is %.2f %, the female students ratio is %.2f %" % (mratio, fratio)
print(sText)
