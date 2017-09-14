class MyFirstClass:     
	variable = 1 # class variable 
 
	def my_first_method(self, arg):
		print(self.variable + arg) # instance variable
		print(self.variable)
		self.variable += 1
		print(self.variable) 

print (MyFirstClass.variable)
var1 = MyFirstClass()
var1.variable = 2;
print (var1.variable)