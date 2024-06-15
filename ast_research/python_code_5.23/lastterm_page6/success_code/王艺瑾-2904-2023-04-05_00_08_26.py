def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
 
   
    aa, aa_sum = 0, 0
    for i in range(1, a+1):
        aa += a * 10**(i-1)
    
        aa_sum += aa
    print(aa_sum)

main()

