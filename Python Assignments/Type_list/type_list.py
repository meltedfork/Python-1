#takes list, prints message based on data type

ex1 = ["potatoes", 25, "explaining fast","turkey day",45,30]
ex2 = ["potatoes","explaining fast","turkey day"]
ex3 = [25,45,30]

def typeCheck(ex_list):
    listLength = len(ex_list) #length of list input
    tempType = type(ex_list[0]) #check data type of list input at index 0
    typeFind ="" #undefined results
    stringSum = ""
    numSum = 0
    

    #for loop to cycle through indices of input
    for x in range(0,listLength):


        if type(ex_list[x]) != tempType:
            typeFind = "The list you entered is of a mixed type"
            break
            #if type of input's index 0 does not equal type of input's index x print typeFind
            
        

        elif isinstance(ex_list[x], str):
            typeFind = "The list you entered is all strings"

            #if type of input[0] is a string and matches input[x], print typefind and add sum of index to stringSum

        elif isinstance(ex_list[x], int):
            typeFind = "The list you entered is all numbers"
            #if type of input[0] is a number and matches input[x], print typefind and add sum of index to numSum

    for x in range(0,listLength):
      
        if isinstance(ex_list[x], str):
            stringSum += ex_list[x] + " "

        if not isinstance(ex_list[x],str):
            numSum += ex_list[x]

        tempType = type(ex_list[x])
        #reset the tempType to the the previous index's data type

    if typeFind == "The list you entered is of a mixed type":
        print typeFind
        print "String sum:", stringSum
        print "Number sum:", numSum

    elif typeFind == "The list you entered is all strings":
        print typeFind
        print "String sum:", stringSum

    elif typeFind == "The list you entered is all numbers":
        print typeFind
        print "Number sum:", numSum
         

typeCheck (ex1)
typeCheck (ex2)
typeCheck (ex3)