se1=input()
se2=input()
hunhe={se1,se2}
zise={"red","yellow"}
lvse={"yellow","blue"}
chengse={"red","yellow"}
total={"red","yellow","purple"}
if se1 not in total or se2 not in total or se1==se2:
    print("error")
elif hunhe==zise:
    print("purple")
elif hunhe==lvse:
    print("green")
elif hunhe==chengse:
    print("orrange")
