from re import A


scores=[]
for i in range(3):
    student={}
    lst1=[]
    lst1=input().split()
    student["name"]=lst1[0]
    student["english"]=eval(lst1[1])
    student["python"]=eval(lst1[2])
    student["math"]=eval(lst1[3])
    student=dict(lst1)
    scores.append(student)
for i in range(3):
    student=scores[i]
    avg=(student["english"]+student["python"]+student["math"])/3
    student["avg"]=round(avg,2)
    scores.sort(key=lambda x:x["avg"],reverse=True)
for x in scores:
    l1=["names:",x["name"],"english;",x["english"],"python:","math:",x["math"]]
    d1=dict(11)
    print(11)



