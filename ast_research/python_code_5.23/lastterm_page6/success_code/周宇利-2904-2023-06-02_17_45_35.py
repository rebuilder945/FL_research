def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
     m=x
     b=x
     list=[]
     while b>1:
           for i in range(2,x+1):
                 n=x*(10**(i-1))+m
                 m=n
                 list.append(m)
                 b-=1
     print(sum(list)+x)
main()

