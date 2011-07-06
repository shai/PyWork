# http://learnpythonthehardway.org/book/ex6.html

# This sets the entire sentence with the substitution into 'x' variable
x = "There are %d types of people." % 10
# Set the variable 'binary' with the string 'binary'
binary = "binary"
# Set the variable below with the string "don't"
do_not = "don't"
# Set 'y' with the text after the substitution
y = "Those who know %s and those who %s." % (binary, do_not) # Extra credit #2

# Print 'x' string
print x
# Print 'y' string
print y

# Print the text as a string after the substitution
print "I said: %r." % x # Extra credit #2
# Print the text as a string after the substitution
print "I also said: '%s'." % y # Extra credit #2

# Set the variable 'hilarious' with the string 'False'
hilarious = False
# Set the variable as a whole without the subsitution
joke_evaluation = "Isn't that joke so funny?! %r" # Extra credit #2

# This line actually does the substitution from the last two lines above
print joke_evaluation % hilarious

# Set 'w' with a string
w = "This is the left side of..."
# Set 'e' with a string
e = "a string with a right side."

# Print both strings
# Extra credit #4: Taking two strings and using the plus (+) sign will
# make them a long string. Taking two integers on the other hand (1 + 2 = 3)
# would do addition. This is an example of polymorphism.
print w + e # Extra credit #3
