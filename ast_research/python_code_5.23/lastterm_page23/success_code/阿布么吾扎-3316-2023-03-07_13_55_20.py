def square(a,b):
    return(a/(a+b))*100,(b/(a+b))*100
a = input()
b = input() 
(m,f)=square(int(a),int(b))
print(m,'%')
print(f,'%')
