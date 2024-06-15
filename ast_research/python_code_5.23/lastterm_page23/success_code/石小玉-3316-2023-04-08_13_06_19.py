fMale=float(input())
fFemale=float(input())
pMale=float(fMale/(fMale+fFemale))*100
pFemale=float(fFemale/(fMale+fFemale))*100
print("The male students ratio is %.2f%,the female students ratio is %.2f%" % (pMale,pFemale))

