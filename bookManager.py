def readFile(filename):
	try:
		result=[]
		f = open(filename, 'r')
		for line in f.readlines():
			dic=dict()
			read=list()
			line.strip()
			line = line[1:line.index('\n')-1]
			read = line.split(',')
			for x in read:
				x.strip()
			dic['name']=read[0][1:-1]
			dic['author']=read[1][1:-1]
			dic['price']=read[2]
			result.append(dic)
		f.close()
	except IOError as err:
		print(err)
	return result

def showFile(input):
	for x in input:
		print(x)


def main():
	input = readFile('book.txt')
	showFile(input)




if __name__=="__main__":
        main()
