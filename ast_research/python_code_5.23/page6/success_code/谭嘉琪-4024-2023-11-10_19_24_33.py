def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
 a1=str(a)
 s=0
 for i in range(a+1):
  a2=a1*(i+1)
  a3=int(a2)
  s=s+a3
 print(s)
main()

