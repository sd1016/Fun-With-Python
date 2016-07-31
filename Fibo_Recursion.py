#This function generates the first n fibonacci numbers
def Fib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return Fib(n-1)+Fib(n-2)


n = int (raw_input("How many Fibonacci numbers you want?"))
for i in range(1,n+1,1):
	print Fib(i)

