color1 = input().lower()
color2 = input().lower()
s1 = {color1,color2}
if color1 != color2:
    if s1 == {"red","blue"}:
        print("purple") 
    elif s1 == {"red","yellow"}: 
        print("orange")
    elif s1 == {"yellow","blue"}: 
        print("green")  
else:
    print('error')



                    




