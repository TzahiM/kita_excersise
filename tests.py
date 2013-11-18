'''

@author: Bracha
'''

def get_hello_string():
    return "Hello World"

print get_hello_string()

def hello_personalize(name):
    return "Hello " + name
    
print hello_personalize("Yoni")

def bottels(nBottles):
    """
    99 bottles of beer on the wall, 99 bottles of beer.
    Take one down and pass it around, 98 bottles of beer on the wall.
    """
    lines = range(0,nBottles)
    for i in range(nBottles):
        num_str = str( nBottles - i)
        line = "% bottles of beer on the wall, % bottles of beer.\n" % num_str, num_str
        line += "Take one down and pass it around, %s bottles of beer on the wall" % num_str
        lines[i] = line
    
    return lines


def print_bottels(nBottles):
    lines = bottels(nBottles)
    for i in range(nBottles):
        print lines[i]
    
print_bottels(7)
 
        
         
    
    
    
    