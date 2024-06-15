numberboy=input("")
numbergirl=input("")
ratioboy=int(numberboy)/(int(numbergirl)+int(numberboy))
ratiogirl=int(numbergirl)/(int(numbergirl)+int(numberboy))
print("The male students ratio is ",'{:.2f}%'.format(ratioboy*100),end=","),print("the female students ratio is",'{:.2f}%'.format(ratiogirl*100))

