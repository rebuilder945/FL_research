def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
      i=0
      while i<x:
            s=s+x
            x=x+10*x
            i=i+1
      print(s)
      
main()

