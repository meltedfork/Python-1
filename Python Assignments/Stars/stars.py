 # part 1

def draw_stars(list):
    for i in list:     
        stars=""                
        for x in range(i):
            stars += "*"
        print stars

input=[4,6,1,3,5,7]

draw_stars(input)



#part 2

def draw_stars(list):
    for i in list: 
        # for
        if isinstance(i, int):    
            stars=""               
            for x in range(i):
                stars += "*"
            print stars
        elif isinstance(i, str):
            letters=""               
            for j in range(len(i)):
                letters += i[0].lower()
            print letters

input=[4,"bacon",1,3,"mangle",7]

draw_stars(input)