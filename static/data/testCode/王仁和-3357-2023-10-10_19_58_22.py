planename=str(input())
a=eval(input())
v=eval(input())
length =float(v * v / (2*a))
print("The acceleration of " + planename+"is"+a+"M / s, the take-off speed is"+v+"M / s, and the shortest take-off runway length is "+length+"M.")
