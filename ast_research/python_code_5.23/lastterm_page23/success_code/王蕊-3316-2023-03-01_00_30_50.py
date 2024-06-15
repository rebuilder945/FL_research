#男女比例.py
iMale=int(input())
iFemale=int(input())
a= iMale / (iMale + iFemale) * 100                                                                                                                                                                       
b= iFemale / (iMale + iFemale) * 100
print("The male students ratio is %.2f%% ,the female students ratio is %.2f%%"%(a,b))

