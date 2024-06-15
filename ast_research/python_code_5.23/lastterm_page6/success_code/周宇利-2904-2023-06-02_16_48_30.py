def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
      a=0
      for i in range(1,x+1):
           b=0
           for j in range(1,i+1):
                b=x*(10**len(str(x)))+x
                a+=b
      print(a)

main()

