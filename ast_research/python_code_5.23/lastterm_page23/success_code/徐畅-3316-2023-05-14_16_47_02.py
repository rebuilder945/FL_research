boy=eval(input())
girl=eval(input())
bili=(boy/(boy+girl))*100
biligirl=100-bili
print("The male students ratio is {:.2f}%,the female students ratio is {:.2f}%".format(bili,biligirl))
