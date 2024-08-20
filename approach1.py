def addop (a,b): #here 'a' and 'b' are called as formal params
    c=a+b # Here 'c' is called as local variable 
    return c # Here return is used for returning the value from function 
#body to function call 

#Main Program 
x=int(input("Enter First Number:"))
y=int(input("Enter Second Number:"))
res = addop (x,y) #Function Call 
print("Sum({},{}={})".format(x,y,res))