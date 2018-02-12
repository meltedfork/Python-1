def my_dict():
    
    about = {
        "Name": "Nick", 
        "Age": "31", 
        "Country of birth": "United States",
        "Favorite Language": "Italian"
        }

    # print about.items()
    for key,data in about.iteritems():
        print "My", key, "is", data

my_dict()