sboy=input()
sgirl=input()
sboy=int(sboy)
sgirl=int(sgirl)
sp=sboy+sgirl
rb=float(sboy/sp)
rg=float(sgirl/sp)
rb=rb*100
rg=rg*100
text="The male students ratio is %.2f%%,the female students ratio is %.2f%%"%(rb,rg)
print(text)
