def inputSize():
	size = input("input diamond size > (if you quit program input 'quit') >>> ")
	return size

def showDiamond(size):
	result=""
	for i in range(size*2):
		if i<=size:
			spaces=size-i
			dia=i
			print(" "*spaces+"x "*dia)
			result+=" "*spaces+"x "*dia+'\n'	
		else:
			spaces=i-size
			dia=2*size-i
			print(" "*spaces+"x "*dia)
			result+=" "*spaces+"x "*dia+'\n'
	return result

def saveDiamond(result):
	try:
		with open('./diamond.txt','w') as f:
			f.write(result)
			f.close()
	except IOError as err:
		print(err)

def firstInit():
	print("\t\t my saved diamond")
	loadDiamond()

def loadDiamond():
	try:
		input_file=open('./diamond.txt','r')
		for line in input_file.readlines():
			print(line)
		input_file.close()
	except FileNotFoundError as err:
		open('./diamond.txt','w')
		print("not saved file in storage")

def checkInput():
	flag = 1
	while(flag):
		size=inputSize()
		try:
			size=int(size)
			if(size%2):
				result=showDiamond(size)
				saveDiamond(result)
			else:
				print("please input odd number")
		except ValueError:
			if(size == "quit"):
				flag=0
				print("saved last diamond")
			else:
				print("not int!")

def main():
	firstInit()
	checkInput()
if __name__=="__main__":
	main()

