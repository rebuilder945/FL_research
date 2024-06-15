iboys=eval(input())
igirls=eval(input())
ipg=igirls/(igirls+iboys)*100
ipb=iboys/(igirls+iboys)*100
print("The male students ratio is %.2f%%, the female students ratio is %.2f%%."%(ipb,ipg))
