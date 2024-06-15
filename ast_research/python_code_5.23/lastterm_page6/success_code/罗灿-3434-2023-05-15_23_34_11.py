base=['red','blue','yellow']
basecolor=["'red','blue'","'red','yellow'","'blue','yellow'"]
outcolor=['purple','orange','green']
color1=input()
color2=input()
if color1==color2 or color1 not in base or color2 not in base:
    print("error")
else:
    for i in range(len(basecolor)):
        if color1 in basecolor[i] and color2 in basecolor[i]:
            print(outcolor[i])

