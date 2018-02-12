def odd_even():
    for count in range (1,2001):
        if count % 2 == 1:
            print "Number is", count, ". This is an odd number"
        if count % 2 == 0:
            print "Number is", count, ". This is an even number."
# odd_even()

def multiply(my_list, value):
    for i in range (len(my_list)):
        my_list[i] *= value
    print my_list
    return my_list 

list1= [2,4,6,8]
num=5

multiply(list1,num)


def multiple_ones(list2):  #new function, takes in list
    newList = []            #blank list
    multList = multiply(list2[0],list2[1]) #multList will equal the result of the input list, with each index multiplied by 2.
    print multList 
    for x in range(len(multList)): #for loop, from 0 to length of MultList, 0-2 in this example
        innerList=[]                #create new list
        for j in range(multList[x]): #for loop, from 0-value at each index of multList
            innerList.append(1)      #at each index, "1" is inserted for each loop
        print innerList
        newList.append(innerList)   #put the inner list inside of the new list
    print newList

test=([2,4,6], 2)

multiple_ones(test)