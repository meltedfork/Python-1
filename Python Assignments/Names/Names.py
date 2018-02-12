#part 1. given list, create output:
# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel

students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]

def names(input_list):  #create function with parameter of list
    for student in students:    #iterate over  each index of list 
        print student["first_name"], student["last_name"]    #print values for keys of first/last names for each iteration of student
names(students)


#part 2 - given following dictionary, create following output:

# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
}

# print 'students'
def names2(input_dict):  #create function
    for title,names in input_dict.items():          #for loop, finds key and values of everything inside input_dict
        print title
        counter = 0                             #counter to prepend name
        for value in names:                      # for loop, searching for specific values within the data
          counter +=1                              
          first_length=len(value["first_name"])     #variable for first name character count
          last_length=len(value["last_name"])       #variable for last name character count
          full_length=first_length+last_length      #variable for first+last name character count
          print "#", counter, value["first_name"], value["last_name"], full_length
        
names2(users)