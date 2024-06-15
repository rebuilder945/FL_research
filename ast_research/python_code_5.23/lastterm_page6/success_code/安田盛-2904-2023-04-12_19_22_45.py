def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
     b=[]
     c=a
     for i in range(1,a+1):
         b.append(str(c)*i)
     s=0
     for i in b:
         s+=int(i)
     print(s)
main()
main()

