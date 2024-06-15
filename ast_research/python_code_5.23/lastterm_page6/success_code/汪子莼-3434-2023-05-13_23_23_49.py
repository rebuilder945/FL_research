color1=input()
color2=input()
color_set=[["red","blue"],["red","yellow"],["blue","yellow"]]
secondary_color=["purplr","orange","green"]
for i in range(len(color_set)):
    if color1 in color_set[i] and color2 in color_set[i]:
        if color1==color2:
            print("error")
            break
        else:
            print(secondary_color[i])
    else:
        print("error")
