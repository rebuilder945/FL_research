pc=['yellow','red','blue']
c1=input()
c2=input()
if c1 in pc and c2 in pc and c1!=c2:
    if c1 in ['blue','yellow'] and c2 in ['blue','yellow']:
        print("green")
    if c1 in ['blue','red'] and c2 in ['blue','red']:
        print("purple")
    if c1 in ['yellow','red'] and c2 in ['yellow','red']:
        print("orange")
else:
    print("error")
