# http://learnpythonthehardway.org/book/ex8.html

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

# Extra credit #2: The 3rd string has a single qoute in it, so it
# will print that whole text, with the double quotes.
