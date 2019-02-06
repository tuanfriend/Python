# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("My name is", name)	# with a comma
print("My name is "+name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print(f"Hello {name}!")	# with a comma
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}".format(fave_food1,fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string
print(f"I love to eat {fave_food1.upper()} and {fave_food2.upper()}") # with an f string
