#Efrain Duarte Lopez
def triangulo(size):
	for i in range(1,size+1):
		for c in range(1,i+1):
			print('T',end="")
		print()
	for i in range(size,0,-1):
		for c in range(1,i+1):
			print('T',end="")
		print()
triangulo(8)
