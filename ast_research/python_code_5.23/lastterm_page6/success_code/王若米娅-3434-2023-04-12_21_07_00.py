c1=input()
c2=input()
lst=[c1,c2]
if 'red' in lst and 'blue' in lst:
    print("purple")
elif 'red' in lst and 'yellow' in lst:
    print("orange")
elif 'yellow' in lst and 'blue' in lst:
    print("green")
else:
    print("error")
