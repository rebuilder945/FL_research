def main():
    a=int(input())
    calculate_sum(a)
    print(calculate_sum(a))
def calculate_sum(a):
    lst=[]
    for i in range(a):
         b=int(str(a)*(i+1))
         lst.append(b)
     calculate_sum(a)=sum(lst)
     return(calculate_sum(a))
main()

