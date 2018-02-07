def coin_toss():
    heads = 0
    tails = 0

    for x in range(5000):
        import random
        num = (random.randint(1, 2))

        if num == 1:
            heads +=1
            print "Throwing a coin...It's a head! ...Got",heads,"head(s) so far and", tails, "tail(s) so far"
        if num == 2:
            tails +=1
            print "Throwing a coin...It's a tail! ...Got",heads,"head(s) so far and", tails, "tail(s) so far"


    print "Ending the program, thank you!"