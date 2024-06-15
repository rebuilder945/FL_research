def print_matrix(n):
        lst= []
        js =1
        for i in range(1,n+1):
              for x in range(n):
                   lst.append(str(js))
                   if js<i:
                        js+=1
              print(" ".join(lst),"\n")
              lst=[]
              js=1

number=eval(input())
print_matrix(number)



