def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
       s=0
       a=str(a)
       for x in range(1,a+1):
          s+=int(a*x)
       print(s)
main()

