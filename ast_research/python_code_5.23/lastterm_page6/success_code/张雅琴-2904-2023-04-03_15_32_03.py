def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=[]
    for i in range (1,a+1):
        c=10**(a-i)
        b.append(i*c)
    total=0
    for ele in range(0,len(b)):
        total+=b[ele]
    return a*total 
a=eval(input())       
print(calculate_sum(a))        

main()

