import random # we'll need the random module to roll the dice
class DicePile:
    def __init__(self, initQuantity, initSides): # constructor
        self.setQuantity(initQuantity)
        self.setSides(initSides)
        self.__rollCount = 0 #private attribute
        #self.rollCount = 0 #public attribute
        self.rolled = False
       

    def __str__(self): # generate a string representation of the object
        
        if self.rolled:
            resultString = str(self.__results)
        else:
            resultString = 'not rolled'
            
        dicescription_var = self.dicescription()
        return dicescription_var + ': ' + resultString + "(roll count: "+ str(self.__rollCount) +")"

    def roll(self): # roll the dice
        self.__results = [] # set results to empty list

        self.__rollCount +=1
        
        for i in range(self.__quantity): # generate random numbers and add to list
            self.__results.append(random.randint(1, self.__sides))
        self.rolled = True

    def getResults(self): # get results list (None if not rolled)
        return self.__results

    def getQuantity(self): # get quantity attribute
        return self.__quantity

    def getSides(self): # get sides attribute
        return self.__sides

    def setQuantity(self, newQuantity): # set quantity attribute
        if int(newQuantity) < 1:
            raise ValueError('dice quantity cannot be less than 1')
        else:
            self.__quantity = int(newQuantity)
            self.__results = None
        self.rolled = False

    def setSides(self, newSides): # set sides attribute
        if int(newSides) < 2:
            raise ValueError('dice sides cannot be less than 2')
        else:
            self.__sides = int(newSides)
            self.__results = None
        self.rolled = False


    def getRollCount(self):
        return self.__rollCount

    def dicescription(self):
        return str(self.__quantity) + 'd' + str(self.__sides)
        


    

    
