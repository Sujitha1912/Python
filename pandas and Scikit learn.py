outputfile1=open("LogFuel.txt", "a")
tankcapacity = 0
gastoad=0
currentlevel=0
miles=int(input("Please Enter Miles per gallon:"))
outputfile1.write("User Input: Miles per gallon:")
outputfile1.write(str(miles))
tankcapacity=int(input("Tank Size (in gallons):"))
outputfile1.write("\nUser Input: tank size:")
outputfile1.write(str(tankcapacity))
drive=miles*tankcapacity#total capacity


def	gastoadd():
	global tankcapacity
	global currentlevel
	print("How much gas to Add:_")
	gastoad=int(input())
	gasmax=tankcapacity-currentlevel
	gastoad=int(gastoad)
	if(gastoad<gasmax):
		currentlevel=currentlevel+gastoad
	else:
		print(" you CANNOT exceed the car’s tank capacity")
		outputfile1.write("\nUser Input:3-Add Gas")
		outputfile1.write("\nAdded gas is:")
		outputfile1.write(str(gastoad))
		outputfile1.write("\nGas to add is more than car tank's capacity")
	outputfile1.write("\nUser Input:3-Add Gas")
	outputfile1.write("\nAdded gas is:")
	outputfile1.write(str(gastoad))
		
def todrive():
	global currentlevel
	global miles
	global drive
	print("How many miles to drive:_")
	todr=int(input())
	if(currentlevel!=0):	
		if(drive>=todr):
			drive=drive-todr
			print("you drove",todr,".you can drive another",drive," on this gas.")
			outputfile1.write("\nUser Input:2-Drive")
			outputfile1.write("\nMiles to Drive:")
			outputfile1.write(str(todr))
			outputfile1.write("\nyou drove,")
			outputfile1.write(str(todr))
			outputfile1.write(".you can drive")
			outputfile1.write(str(drive))
			outputfile1.write("on this gas")
		else:
			print("miles to drive is more than the cars capacity which is.\n Please choose within the range. Have a safe trip!")
			outputfile1.write("\nUser Input:2-Drive")
			outputfile1.write("\nMiles to Drive:")
			outputfile1.write(str(todr))
			outputfile1.write("\nMiles to drive input is more than cars capacity")
	else:
		print("Need to Fill gas to proceed to drive")
		outputfile1.write("\nUser Input:2-Drive")
		outputfile1.write("\nMiles to Drive:")
		outputfile1.write(str(todr))
		outputfile1.write("\nNeed to Fill gas to proceed to drive")
			
def currentfuellevel():
	global currentlevel
	print("current Fuel level:\n",currentlevel)
	outputfile1.write("\nUser Input:1- see current fuel level\nFuel level shown:")
	currentfuellevel=currentlevel
	outputfile1.write(str(currentfuellevel))
	
while True:
	print("*"*70,"\nwhat would you like to do:\n1. See Current Fuel Level\n2. Drive\n3. Add Gas\n4. Exit")#displaying this to get the input from the user
	user=str(input())
	if(user=="1"):
		currentfuellevel()
	elif(user=="2"):
		todrive()
	elif(user=="3"):
		gastoadd()
	elif(user=="4"):
		outputfile1.write("\nUser Input:4-Exit")
		break
		
