color1=input()
color2=input()
color_set=[["red","blue"],["red","yellow"],["blue","yellow"]]
secondary_color=["purple","orange","green"]
flag=0
for i in range(len(color_set)):
    if color1==color2:
        break
    if color1 in color_set[i] and color2 in color_set[i]:
            print(secondary_color[i])
            flag=1
            break
if flag==0:
    print("error")
