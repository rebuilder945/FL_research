grade = {"A":"A","B":"B","C":"C","D":"D","E":"E"}
scores = eval(input())
if scores >= 90:
    print(grade["A"])
elif scores >= 80 and scores < 90:
    print(grade["B"])
elif scores >= 70 and scores < 80:
    print(grade["C"])
elif scores >= 60 and scores < 70:
    print(grade["D"])
else:
    print(grade["E"])
