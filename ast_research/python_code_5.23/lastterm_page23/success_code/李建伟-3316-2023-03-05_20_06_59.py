m = float(input("请输入男生人数："))
w = float(input("请输入女生人数："))
Mrate = m/(m+w)*100
Wrate = w/(m+w)*100
print("The male students ratio is %.2f%%,the female students ratio is %.2f%%"%(Mrate, Wrate))
