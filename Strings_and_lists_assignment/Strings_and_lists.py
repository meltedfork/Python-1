words = "It's Thanksgiving day. It's my birthday, too!"

print words.find("day")

new_words = words.replace("day","month")
print new_words

x = [2,54,-2,7,12,98]

print max(x)
print min(x)

z = ["hello",2,54,-2,7,12,98,"world"]
print z[0], z[len(z)-1]

p = [19,2,54,-2,7,12,98,32,10,-3,6]

p.sort()
print p

p1 = p[0:5]
p2 = p[5:11]

print p1
print p2

newp = p2
print newp
newp.insert(0,p1)

print newp

