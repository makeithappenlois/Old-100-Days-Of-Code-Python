number = int(input("Number:"))

if number<0 or number>0:
	result = str(number) + " is now " + str(-1*number) + "."
else:
	result = "Can't touch. Number is " + str(0)

print(result)
