men=eval(input())
women=eval(input())
mratio=100*men/(men+women)
wratio=100*women/(men+women)
print("The male students ratio is {:.2f}%, the female students ratio is {:.2f}%".format(mratio,wratio))

