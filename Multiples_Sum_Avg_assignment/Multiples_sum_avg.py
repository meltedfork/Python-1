#prints odd numbers from 1-1000

for counter in range(0,1001):
    if counter % 2 == 1:
        print counter


#prints multiples of 5 from 5 to 1,000,000

for fives in range(5,1000001):
    if fives % 5 == 0:
        print fives

#prints sum of given list
a = [1,2,5,10,255,3]
b= sum(a)
print b

#average of list a

avg = b/len(a)
print avg