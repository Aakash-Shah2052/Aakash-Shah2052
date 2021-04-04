a = 10
b = 20
op = input("What operation do you want to perform?")

if op == 'sum':
    print("Sum is", a+b)
    
elif op == 'multiply':
    print("Multiplication is", a*b)   
    
elif op == 'divide':
    print("Division is", a/b)
    
elif op == 'substract':
    print("Difference is", a-b)

else:
   print("we only perform the operation like sum, multiply, divide, substract")