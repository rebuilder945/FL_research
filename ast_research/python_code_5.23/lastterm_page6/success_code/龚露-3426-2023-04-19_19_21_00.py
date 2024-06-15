def final(x):
    if x<20:
        return 6*x*x+1
 
    if 20<=x<40:
        return (3*x-60)**1/2
  
    if x>=40:
       return 100/(x+1)
    
x = eval(input())
print("%.2f"%final(x))

