
ladoOne = int(input(""))
ladoTwo = int(input(""))
ladoThree = int(input(""))

if ladoTwo != ladoOne and ladoTwo>ladoThree:
	print("escaleno")
elif ladoThree == ladoTwo and ladoThree != ladoOne:
	print("Equilatero")
elif ladoOne == ladoThree and ladoOne != ladoTwo:
	print("isoceles")	
