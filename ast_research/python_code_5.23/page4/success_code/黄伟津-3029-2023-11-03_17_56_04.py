lname = input()
lname = lname.split(",")
lscore = eval(input())
lst = [ [a,b] for a,b in zip(lname,lscore)]
print(lst)


