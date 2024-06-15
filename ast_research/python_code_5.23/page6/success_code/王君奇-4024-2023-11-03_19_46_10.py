def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
      s=0
      for i in range(1,a+1):
           c=0
           for j in range(i):
                c+=10**j
                s+=a*c
      print(s)
main()

