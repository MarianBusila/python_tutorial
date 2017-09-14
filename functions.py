#functions
def myfunc():
	print(1)
	print(2)
	print(3)

print(5)
myfunc()
# 5
# 1
# 2
# 3

print ("*" * 30)
def myfunc2(p1, p2):
	print(p1*3)
	print(p2*3)

myfunc2(1,2)
myfunc2(1, "Me")
# 3
# 6
# 3
# MeMeMe

print ("*" * 30)
def myfunc3(p1, p2, *args):
	print(p1)
	print(p2)
	print(args)

myfunc3(1,"Me", 4, 5, 6)
# 1
# Me
# (4, 5, 6)

print ("*" * 30)
#**args is a dictionary of parameters 
def f1(var, trace = False):
	if trace: print ("Useful trace")
	print (var)
	
def f2(var, **args):
	f1 (var * 2, **args)

def f3(var, **args):
	f2 (var * 3, **args)
	
def f4(var, **args):
	f3 (var * 4, **args)
	
f4(10, trace=True)
	