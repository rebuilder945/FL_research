def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    a=int(input())
    b=[]
    for i in range (1,a+1):
        c=10**(a-i)
        b.append(i*c)
    total=0
    for ele in range(0,len(b)):
        total+=b[ele]
       d= a*total 
       print(d)        

main()

