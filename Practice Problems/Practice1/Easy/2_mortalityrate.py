years = int(input("Input number of years of your degree program:"))
numFreshies = int(input("Input number of freshies:"))
mortalityRate = float(input("Input mortality rate(%):"))/100

numSurvivors = int(numFreshies*((1-mortalityRate)**years))

print("Survivors: " + str(numSurvivors))
