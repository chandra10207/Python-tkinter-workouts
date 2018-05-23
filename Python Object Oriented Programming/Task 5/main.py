import dice # import the module containing the class

myDice = dice.DicePile(4, 6) # create an object
myDice.roll() # call the roll method
print(myDice) # use the __str__ method
myDice.setQuantity(8) # change the quantity
myDice.setSides(20) # change the sides
print(myDice.getResults()) # notice the results are now None
myDice.roll() # roll the dice again
print(myDice.getResults()) # show the results

# Testing Roll  Count
#print("Roll Count Testing\n\t","Roll Count: ",myDice.getRollCount())

#if myDice.rolled:
# print('\nThe dice have been rolled!')




