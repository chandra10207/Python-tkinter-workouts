import os

# --- getList(filename), returns a list of strings ---
# (open/create file and return lines of text as a list of strings)
def getList(filename):
    data = [] # this line is a placeholder
    #print("Reading file:",filename)
    file_exist = os.path.isfile('./'+filename)
    
    if(file_exist):        
        #print("found")
        f = open(filename, 'r')        
        data = f.readlines()
        f.close()
        #print(data)        
    else:
        #print("File Not Found!! Created a new file")
        f = open(filename, 'w+')        
        data = f.readlines()
        f.close()
        #print(data)        
    return data






# --- showList(data), returns nothing ---
# (receive list of strings and display them, or "nothing in list" message)
def showList(data):
    #print("Printing list\n")
    #print(len(data))
    list_length = len(data)
    if(list_length > 0):
        print("To Do List:\n")
        index = 1
        for element in data:
            print ('    {}) {}'.format(index, element.rstrip()))
            index += 1
    else:
        print("Your To Do List is empty.")
        

 

# --- addToList(filename, data), returns a list of strings ---
# (prompt for an item to add to the list of strings and append to the file)
def addToList(filename, data):
    item = input("Add: ")
    data.append(item)
    f = open(filename, 'a')
    f.write(item)
    f.write("\n")  
    #data = f.readlines()
    f.close()
    print("Item added to list.")   
    return data





# --- deleteFromList(filename, data), returns a list of strings ---
# (prompt for item number to delete from the list of strings and write list to the file)
def deleteFromList(filename, data):
    item_to_delete = input("Item number to delete: ")
    try:
        item = int(item_to_delete)        
        if(item <= len(data)):
            actual_item = item - 1            
            #data.pop(actual_item)
            del data[actual_item]
            print(data)
            f = open(filename,"w")            
            i = 0
            for item in data:
                f.write(item + "\n")
                i+=1
            f.close()
            print("Item deleted from list")
            #print(data)
        else:
            print("Please enter valid value")
            
        
    except ValueError:
        print("Please enter valid value")
    return data



# --- main part of program ---
FILENAME = 'list.txt' #define the filename used to store the list
lineList = getList(FILENAME) # call the getList function to read the file into a list
#print(lineList)


while True: # this endless loop displays the list and prompts the user for a command
 showList(lineList) # call showList to show the current content of the list
 # show the instructions for the possible commands - [a]dd, [d]elete, e[x]it
 print('\nType "a" to add an item.')
 if len(lineList) > 0: # only show the delete instruction if the list has items
     print('Type "d" to delete an item.')
 print('Type "x" to exit.')
 command = input('> ') # prompt for a command
 # if "a", calladdToList to prompt for item and add to list
 if command == 'a':
     lineList = addToList(FILENAME, lineList)
 # if "d", call deleteFromList to prompt for item number and delete from list
 elif command == 'd' and len(lineList) > 0:
     lineList = deleteFromList(FILENAME, lineList)
 elif command == 'x': # if "x", break out of the loop to end the program
     print('Goodbye!')
     break
 else: # if anything else, show an error message
     print('Invalid command.\n')



     
