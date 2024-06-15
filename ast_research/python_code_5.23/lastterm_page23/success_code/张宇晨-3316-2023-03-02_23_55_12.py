cMale=int(input())
cFemale=int(input())
zMale=cMale/(cMale+cFemale)*100
zFemale=cFemale/(cMale+cFemale)*100
print("The male students ratio is %.2f%,the female students ratio is %.2f%"(zMale,zFemale))
