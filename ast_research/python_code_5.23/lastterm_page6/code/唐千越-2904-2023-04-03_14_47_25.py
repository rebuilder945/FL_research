def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
      sum = 0
     for i in range(a):
          n=10^i
          a=n*a+a    
          sum  +=a
     print(sum)  

main()

