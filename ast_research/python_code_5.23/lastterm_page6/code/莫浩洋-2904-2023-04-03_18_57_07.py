def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(x):
        s=0
        s1=0
        for i in range(x):
              s+=int(str(x)*(i+1))
              s1+=s
         print(s1)
       
main()

