
while True:
    data = input()
    if data== "ok":
        break
country = data.split(" ")[0]
num = int(data.split(" ")[1])

print(country.sort())
print(num.sort())
for i in country:
    if i =="India":
        print("yes")
    else:
        print("no")
print(sum(num))
