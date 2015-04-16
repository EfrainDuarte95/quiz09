#Efrain Duarte Lopez
def hipotenusa(x1,y1,x2,y2):
	a=x2-x1
	b=y2-y1
	c=((a*a)+(b*b))**0.5

	return c

q=int(input("ingrese la cordenada en x del primer punto: "))
w=int(input("ingrese la cordenada en y del primer punto: "))
e=int(input("ingrese la cordenada en x del segundo punto: "))
r=int(input("ingrese la cordenada en y del segundo punto: "))
t=hipotenusa(q,w,e,r)
print(t)
