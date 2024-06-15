def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
       s=0
       c=0
       m=a
       while c<a:
                s+=m*a*10**c
                c+=1
                m-=1
       print(s)
main()

