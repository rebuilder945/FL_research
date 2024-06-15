cities = {
	"shanghai":{"area":"southeast China","population":2400,"fact":"SH is the modu city of China"},
	"beijing":{"area":"north China","population":3200,"fact":"BJ is the capital city of China"},
	"shenzhen":{"country":"south China","population":2200,"fact":"SZ is the near Hong Kong"}
}

for city in cities:
	print("the infomation of the city " + city.title() + " is as belows:")
	for k,v in cities[city].items():
		print(k+":"+str(v))
	print("***********************")

