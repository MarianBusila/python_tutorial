from collections import deque
from math import pi

def list_as_stack():
    print '*** list_as_stack ***'
    stack = [3, 4, 5]
    print stack
    stack.append(6)
    stack.append(7)
    print stack
    stack.pop()
    print stack

def queue_example():
    print '*** queue_example ***'
    queue = deque(["Eric", "John", "Michael"])
    print queue
    queue.append("Terry")
    queue.append("George")
    print queue
    queue.popleft();
    print queue;
    
def mod3or5(x):
    return x % 3 == 0 or x % 5 == 0 
def filter_example():
    print '*** filter_example ***'
    print filter(mod3or5, range(2, 25))
    
def cube(x):    
    return x * x * x;
def add(x, y):
    return x + y
def map_example():
    print '*** map_example ***'
    print map(cube, range(1, 11))
    seq1 = [2, 4, 6, 8]
    seq2 = [1, 3, 5 ,7]
    print map(add, seq1, seq2)
    
def reduce_example():
    print '*** reduce_example ***'
    print reduce(lambda x, y: x + y, range(1, 11))
    
def list_comprehensions():
    print '*** list_comprehensions ***'
    squares = [x**2 for x in range(10)]
    print squares
    
    print [ (x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    
    print [str(round(pi, i)) for i in range(1, 6)]
    
def del_statement():
    print '*** del_statement ***'
    a = range(1, 10)
    del a[0]
    print a
    del a[2:4]
    print a
    
def tuple_example():
    print '*** tuple_example ***'
    empty = ()
    singleton = 'hello', #notice trailing comma for typle with one element
    print len(empty)
    print len(singleton)
    t = 1234, 4321, 'hello' # tuple packaging
    print t
    a, b, c = t #sequence unpacking
    print a, b, c
    
def set_example():
    print '*** set_example ***'
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    fruit = set(basket) # create a set without duplicates
    print fruit
    print 'orange' in fruit # fast membership testing
    
    a = set('abracadabra')
    b = set('alacazam')
    
    print a - b #letters in a but not in b
    print a | b #letters in either a or b
    print a & b #letters in both a and b
    print a ^ b #letters in a or b but not both
    
    print {x for x in 'abracadabra' if x not in 'abc'} # set comprehension
    
def dictionaries_example():
    print '*** dictionaries_example ***'
    tel = {'jack': 4098, 'sape': 4139}
    tel['guido'] = 4127
    print tel
    print tel.keys()
    print 'guido' in tel
    
    print dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) # another way of defining a dict    
    print dict(sape=4139, guido=4127, jack=4098) # another way of defining a dict
    
    print {x: x**2 for x in (2, 4, 6)} #dict comprehension
    
def looping_techniques():
    print '*** looping_techniques ***'
    #enumarate
    for index, value in enumerate(['tic', 'tac', 'toe']):
        print index, value
        
    #zip
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print 'What is your {0}? It is {1}.'.format(q, a)
        
    #reversed
    for i in reversed(xrange(1, 10, 2)):
        print i,    
    print
    
    #sorted
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(set(basket)):
        print f,        
    print
    
    #iteritems for dictionaries
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.iteritems():
        print k, v
        
def compare_sequences():
    print '*** compare_sequences ***'
    print (1, 2, 3) < (1,2, 4) #true
    print [1, 2, 3] < [1,2, 2] #false
        
def main():
   list_as_stack()
   queue_example()
   filter_example()
   map_example()
   reduce_example()
   list_comprehensions()
   del_statement()
   tuple_example()
   set_example()
   dictionaries_example()
   looping_techniques()
   compare_sequences()

if __name__ == "__main__":
    main()	