
#  Input  the  names  and  scores  of  students
names  =  input().split(',')
scores  =  list(map(int,  input().split(',')))

#  Create  an  empty  list  to  store  the  nested  list
nested_list  =  []

#  Iterate  through  the  names  and  scores  lists,  combining  them  into  nested  lists  and  appending  them  to  the  new  list
for  name,  score  in  zip(names,  scores):
     nested_list.append([name,  score])

#  Output  the  new  nested  list
print(nested_list)

