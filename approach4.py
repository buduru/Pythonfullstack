def addop():
    x=float(input("Enter First Number:"))
    y=float(input("Enter Second Number:"))
    z=x+y
    return x,y,z #in python return can return one or more number of values
#Main Program 
r,m,o =  addop() #Function Call with Multi Line Assingment
print("sum({},{}={})".format(r,m,o))
print("-----------------or-----------------")
hyd =addop() #Function Call -- here hyd is an object 
print("Sum({},{}={})".format(hyd[0],hyd[1],hyd[2]))
