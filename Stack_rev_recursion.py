'''Python program to reverse a 
stack using recursion'''

#Below is a recursive funtion that inserts an element
#at the bottom of a stack.
def insertAtBottom(stack,item):
	if isEmpty(stack):
		push(stack, item)
	else:
	     temp = pop(stack)
	     insertAtBottom(stack,item)
	     push(stack, temp)	


#Below is a funtion thatt reverses a stack using 
#insertAtBottom()
def reverse(stack):
	if not isEmpty(stack):
		temp = pop(stack)
		reverse(stack)
		insertAtBottom(stack,temp)
     


#Functon to create a stack
#Intialized to 0
def createStack():
	stack = []
	return stack

#Function to check if the stack is empty
def isEmpty( stack ):
	return len(stack) == 0

#Function to append an item to the stack
def push( stack, item ):
	stack.append(item)

#Function to pop an item 
def pop( stack ):
	if (isEmpty( stack )):
		print("Stack Underflow")
		exit(1)
	return stack.pop()	

#Function to print the stack
def prints(stack):
	for i in range(len(stack)-1, -1, -1):
		print (stack[i])
		
# Driver program to test above functions
 
stack = createStack()
push( stack, str(8888) )
push( stack, str(777 ) )
push( stack, str(66) )
push( stack, str(5) )
push( stack, str(4) )
push( stack, str(3) )
push( stack, str(2) )
push( stack, str(1) )
print("Original Stack ")
prints(stack)	

reverse(stack)
print("=============") 
print("Reversed Stack ")
print("=============")
prints(stack)	


