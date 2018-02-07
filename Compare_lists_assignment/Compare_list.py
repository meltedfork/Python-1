one = [1,2,5,6,2]
two = [1,2,5,6,2]
list_1 = [1,2,5,6,2]
list_2 = [1,2,5,6,2,3]
first =["celery","carrots","bread","milk"]
second = ["celery", "carrots","bread","cream"]

def Compare (first_list,second_list):
    if first_list == second_list:
        print "The lists are the same"

    else:
        print "The lists are NOT the same"

Compare (first, second)
Compare (one, two)
Compare (list_1, list_2)