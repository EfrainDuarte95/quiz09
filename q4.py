#Efrain Duarte Lopez
def fib(n):
	if n==0 or n==1:
		return n
	else:
		a=0
		b=1
		for i in range(n-1):
			c=a+b
			a=b
			b=c
		return c

# tests added by Ken
print(fib(0))
print(fib(10))
