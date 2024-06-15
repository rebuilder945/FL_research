def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
     x=1
     s=0
     while a>0:
          s=a*x*10**(a-1)+s
          a=a-1
          x=x+1
      print(s)
main()

