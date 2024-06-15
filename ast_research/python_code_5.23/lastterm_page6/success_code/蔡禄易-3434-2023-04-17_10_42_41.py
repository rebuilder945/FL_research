yuan1 = input()
yuan2 = input()
pc = {"red","blue","yellow"}
pc1 = {"red","blue"}
pc2 = {"red","yellow"}
pc3 = {"blue","yellow"}
s1 = {yuan1,yuan2}
if yuan1 not in pc or yuan2 not in pc or yuan1 == yuan2:
    print("error")
elif s1 == pc1:
    print("purple")
elif s1 == pc2:
    print("orange")
else:
    print("green")
