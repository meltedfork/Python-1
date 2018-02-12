def finals():
    for x in range(0,10):
        import random
        num = (random.randint(1, 100))


        if num >= 90:
            print "Score:",num, "; Your grade is A"

        elif num >= 80:
            print "Score:",num,"; Your grade is B"

        elif num >= 70:
            print "Score:",num ,"; Your grade is C"

        elif num >= 60:
            print "Score:",num, "; Your grade is D"

        elif num < 60:
            print "Score:",num, "; Your grade is F"
    
    print "End of program. Bye!"

finals()