def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
       sum=0
       s=str(a)
       tmp=s
       for i in range(a):
          sum+=int(tmp)
          tmp+=s
       print(sum)    

main()

