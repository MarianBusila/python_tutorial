var = 0 == False
var2 = 1 == True
var3 = 2 == False
var4 = 2 == True

print (var) # true
print (var2) # true
print (var3) # false
print (var4) # false

print (type(var)) #class bool

#string
var5 = """my long
string 
on 
different lines"""

print (var5)

print (var5[0]) #m
print (var5[-1]) #s

var6 = "My long string"
print (var6[0:4]) #'My l'
print (var6[3:2]) #'' - nothing
print (var6[3:3]) #'' - nothing
print (var6[3:-3]) #'long str'
print (var6[1:-1]) #'y long strin'
print (var6[:]) #'My long string'
print (var6[::2]) #'M ogsrn' - from beggining to end step 2
print (var6[::-1]) #'gnirts gnol yM' - reverse string
print (var6[::-2]) #'git nly' - reverse string step 2

print("Marian" * 3)  #MarianMarianMarian
print ("+" + "-" * 30 + "+" )
