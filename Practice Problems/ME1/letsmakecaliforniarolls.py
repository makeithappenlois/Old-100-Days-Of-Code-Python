#Let's Make California Rolls!

#Problem
#  Next week’s the birthday of your crush in class, and since you 	
#  know that your crush loves eating California maki, you rally your 
#  classmates to make California rolls to serve for his/her 
#	birthday. You then tell your classmates to buy ingredients given 	#	a recipe

#	The problem is that your instructions were unclear; they bought a 
#	varying amount of each ingredient in the recipe resulting in 
#	possible leftover ingredients

# You now want to find out how many rolls you can make at most given 
# the amount of ingredients on hand and how much leftover 
# ingredients you will be having.

# Recipe ​ (makes ​2 ​ rolls; we can a single roll with ​half ​ the ingredients)
#	 4/5 or 0.8 ​ cup of sushi rice
#	 1 ​ nori (seaweed) sheet
#	 6 ​ surimi (imitation crab) sticks
#	 1/2 or 0.5 ​ avocado
#	 Optional: ​ black/white sesame seeds and masago (Capelin roe)
# We can make an odd number of rolls

#Input
#	In order:
#		Cups of sushi rice (fractional number)
#		Sheets of nori (whole number)
#		Crabsticks (whole number)
#		Avocado (whole number)

#Output
#	The maximum number of rolls possible with the amount of ingredients


cups_SushiRice = float(input("Cups of rice: "))
sheets_Seaweed = int(input("Sheets of seaweed: "))
crabsticks = int(input("Crabsticks: "))
avocado = int(input("Avocado: "))

supply_SushiRice = cups_SushiRice//0.4
supply_Seaweed = sheets_Seaweed
supply_Crabsticks =  
