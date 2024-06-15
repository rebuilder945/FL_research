password = input() 
stars = 0 

if any(char.isdigit() for char in password):
    stars += 1

if any(char.islower() for char in password):
    stars += 1

if any(char.isupper() for char in password):
    stars += 1

if len(password) >= 8:
    stars += 1

special_chars = "~!@#$%^&*()_=-/,.?<>;:[]{}|\\"
if any(char in special_chars for char in password):
    stars += 1

print(stars)
  
