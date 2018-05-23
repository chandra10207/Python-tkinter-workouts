students = {60254: 'John Smith', 60255: 'Gert Du-Cart', 60256: 'Sun Po', 60257: 'Bort Woods', 60258: 'Andrew Butters', 60259: 'Betty Ho'}

#usernames = []
usernames = dict()
for index, student in enumerate(students):

    student_id = student
    student_name = students.get(student)
    #print(student_id,student_name)
    
    fullname = student_name.split()
    first_name = fullname[0]
    last_name = fullname[1]
    lname_nodash = last_name.replace('-',"")
    #print(last_name)
    #print(lname_nodash)
    
    f_lower = first_name.lower()
    l_lower = lname_nodash.lower()
    first_char = f_lower[:1]
    l_char = l_lower[:4]
    #print(type(l_char))
    #l_char.ljust(4, '0')

    if(len(l_char)< 4):
        l_char = l_char.ljust(4, '0')
        
    username = first_char + l_char
    usernames[student_id] = username


#print(usernames)
for index,username in enumerate(usernames):
    student_id = username
    username = usernames.get(username)
    print(student_id,' ',username)
 
        
    

  




















 





































































































































      


























          
        
    
   
    

    

    
    


