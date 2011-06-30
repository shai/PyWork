# http://learnpythonthehardway.org/book/ex4.html

# 100 cars
cars = 100
# 4 spaces in a car
space_in_a_car = 4.0
# 30 drivers
drivers = 30
# 90 passengers
passengers = 90
# cars not driven because they don't have drivers
cars_not_driven = cars - drivers
# cars driven by drivers
cars_driven = drivers
# how many passengers can be given a ride with the amount of cars driven
carpool_capacity = cars_driven * space_in_a_car
# average passengers in each car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
