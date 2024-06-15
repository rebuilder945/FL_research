def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    
    b=str(a)
    for i in range(2,a+1):
          c=b*i
          d=int(c)
          a=a+d
    print(a)
main()

