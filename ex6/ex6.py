#various string operations

#Use the %r for debugging, since it displays the "raw" data of the variable, but the others are used for displaying to users.
#Also you can use %r to refer to any varaible type strings, integers, boolean etc. 

x = "There are %d types of people."% 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x #single quotes not needed with %r. It is automatically added when %r refers to a string. 
print "I also said: '%s'." % y #single quotes needed with %s.

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e #string concatenation operation with + operator.
