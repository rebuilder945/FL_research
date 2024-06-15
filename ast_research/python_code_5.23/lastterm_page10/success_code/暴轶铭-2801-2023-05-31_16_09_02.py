def check_length(password):
    global grade
    if len(password) >= 8:
        grade += 1
    return grade

lst = ["~",'!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','[',']','}','{','|','\\']
def check_mark(password):
    global grade
    for c in password:
        if c in lst:
             grade += 1
             break
    return grade
lst1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def check_lower(password):
    global grade
    for x in password:
        if x in lst1:
            grade += 1
            break
    return grade

lst2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def check_upper(password):
    global grade
    for x in password:
        if x in lst2:
            grade += 1
            break
    return grade

lst3 = ["1","2",'3','4','5','6','7','8','9']
def check_num(password):
    global grade
    for x in password:
        if x in lst3:
            grade += 1
            break
    return grade

password = input()
global grade
grade = 0
check_length(password)
check_mark(password)
check_lower(password)
check_upper(password)
check_num(password)
print(grade)
