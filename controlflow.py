def if_statement():
    print '*** if_statement ***'
    # x = int(raw_input("Please enter an integer:"))
    x = 8
    if x < 0:
        x = 0
        print 'Negative changed to zero'
    elif x == 0:
        print 'Zero'
    elif x == 1:
        print 'Single'
    else:
        print 'More'

def for_statement():
    print '*** for_statement ***'
    words = ['cat', 'window', 'jump']
    for w in words:
        print w, len(w)

def range_statement():
    print '*** range_statement ***'
    a = ['Mary', 'had', 'a', 'little', 'lamb']
    for i in range(len(a)):
        print i, a[i]

def break_statement():
    print '*** break_statement ***'
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print n, 'equals', x, '*', n/x
                break;
        else:
            # loop fell through without finding a factor
            print n, 'is a prime number'

def fibonnaci(n):
    print '*** fibonnaci ***'
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a,b = b, a + b
    return result

def keyword_arguments(name, age=10, sin='ABC'):
    print '*** keyword_arguments ***'
    print 'Name: ', name,
    print 'Age: ', age,
    print 'Sin: ', sin
        
def lambda_statement(n):
    print '*** lambda_statement ***'
    return lambda x: x + n
    
def main():
    if_statement()
    for_statement()
    range_statement()
    break_statement()
    fibs = fibonnaci(2000)
    keyword_arguments('Alex', 6)
    keyword_arguments(age=6, name='Andreea', sin='XYZ')    
    # unpack arguments
    argsDict = {'sin': 'SIN', 'name': 'Marian', 'age' : 37}
    keyword_arguments(**argsDict)
    
    #lambda
    f = lambda_statement(42)
    print f(1)
    print f(2)
    print fibs

if __name__ == "__main__":
    main()		