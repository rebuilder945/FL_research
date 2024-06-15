a=input()
count=0
if len(a)>7:
    count+=1
for x in a:
    if "0"<=x<="9":
        count+=1
    if "a"<=x<="z":
        count+=1
    if "A"<=x<="Z":
        count+=1
    if x in "~!@#$%^&*()_=-/,.?<>;:[]{|\}":
        count+=1
print(count)
