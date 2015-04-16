#Efrain Duarte Lopez
def superpower(a,b):
	c=a%1
	d=b%1
	if c==0 and d==0:
		t=a
		for i in range(b-1):
			c=a*t
			a=c
		return c

	else:
		print("sorry the numbers have to be integers")

x=int(input("ingrasa un numero: "))
y=int(input("ingresa otro numero: "))
z=superpower(x,y)
print(z)
