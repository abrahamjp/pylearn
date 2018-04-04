
#A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory. Let us get to it step by step

def my_name(name, time_of_day):
	def morning():
		print "Hi {} Good Morning!".format(name)

	def evening():
		print "Hi {} Good Evening!".format(name)

	def night():
		print "Hi {} Good Night!".format(name)

	if time_of_day == "morning":
		return morning
	elif time_of_day == "evening":
		return evening
	elif time_of_day == "night":
		return night
	else:
		return morning

greet_morning = my_name("Alfred","morning")
greet_noon = my_name("Andrew","evening")
greet_evening = my_name("Philip","night")

greet_morning()
greet_noon()
greet_evening()

#A def is executed at runtime, hence the memory ref of nested function change over time
#example

def calc(fno,sno,ops):

	def add(fno,sno):
		return fno + sno
	if ops == "+":
		print add
		return add(fno,sno)


calc(11,22,"+")
calc(12,22,"+")
calc(10,20,"+")

#A function is said to be first class if the function can be passed around like an object
