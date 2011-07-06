# http://learnpythonthehardway.org/book/ex5.html

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
centimeters_in_inch = 2.54 # Extra credit #4
weight = 180 # lbs
pounds_in_kilogram = 2.20462262 # Extra credit #4
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That's %f centimeters tall." % (height * centimeters_in_inch) # Extra credit #4
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "%d pounds is %f kilograms." % (weight, weight / pounds_in_kilogram) # Extra credit #4
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it excactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
