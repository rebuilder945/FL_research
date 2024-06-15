name = input().split(",")
name = list(map(str,name))
grades = input().split(",")
grades = list(map(int,grades))
name_grades = []
end = []
for i in range(len(name)):
    name_grades = [name[i],grades[i]]
    end.append(name_grades)
    end.sort(key=lambda x:x[1])
print(end)
    

        
    
