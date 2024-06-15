def classify(name,grades):
    lst=[]
    for i in range(len(name)):
        lst.append([name[i],int(grades[i])])
    lst.sort(key=lambda x:x[1],reverse=True)   
    print(lst) 
a=input().split(",")
b=input().split(",")
classify(a,b)
