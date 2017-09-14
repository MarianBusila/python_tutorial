#tuples

tuple = (1, 2, 3)
print  ( type (tuple) )

#list
list = [1, 2, 3]
print  ( type (list) )

mylist = [1,2 ,3, 4, 5, 6, 7, 8, 9, 0]
mylist[2:4] = ['a', 'b', 'c', 'd']
print (mylist)

#set
myset = {1, 2, 3}
print  ( type (myset) )

#dictionary
mydict = {'key1' : 1, 'key2' : 2, }
print  ( type (mydict) )

#comprehansions
list1 = [i for i in range(10)]
list1 = [i for i in range(10) if i % 2 != 0]
print (list1)