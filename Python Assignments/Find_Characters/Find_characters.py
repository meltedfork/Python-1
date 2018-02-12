words = ["howdy","okay","wrangle","presents","Easter","rats"]
character = "a"
new_list=[]

def findChar (input_list, char):
    i=0
    while i < len(input_list):
        i+=1

        if char in input_list[i]:
            new_list.append(input_list[i])
            print new_list

findChar(words, character)
