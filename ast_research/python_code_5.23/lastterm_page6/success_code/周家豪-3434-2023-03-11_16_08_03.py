def calculate(a,b):
    lst=["red","yellow","blue"]
    if color1==color2 or color1 not in lst or color2 not in lst:
        return "error"
    elif (color1=='red' and color2=='yellow') or (color2=='red' and color1=='yellow'):
        return "orange"
    elif (color1=='red' and color2=='blue') or (color2=='red' and color1=='blue'):
        return "purple"
    else:
        return "green"

color1=input()
color2=input()
print(calculate(color1,color2))


