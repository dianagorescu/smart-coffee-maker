"""
A command-line controlled coffee maker.
"""

import sys
import io


"""
Implement the coffee maker's commands. Interact with the user via stdin and print to stdout.

Requirements:
    - use functions
    - use __main__ code block
    - access and modify dicts and/or lists
    - use at least once some string formatting (e.g. functions such as strip(), lower(),
    format()) and types of printing (e.g. "%s %s" % tuple(["a", "b"]) prints "a b"
    - BONUS: read the coffee recipes from a file, put the file-handling code in another module
    and import it (see the recipes/ folder)

There's a section in the lab with syntax and examples for each requirement.

Feel free to define more commands, other coffee types, more resources if you'd like and have time.
"""

"""
Tips:
*  Start by showing a message to the user to enter a command, remove our initial messages
*  Keep types of available coffees in a data structure such as a list or dict
e.g. a dict with coffee name as a key and another dict with resource mappings (resource:percent)
as value
"""

# Commands
EXIT = "exit"
LIST_COFFEES = "list"
MAKE_COFFEE = "make"  #!!! when making coffee you must first check that you have enough resources!
HELP = "help"
REFILL = "refill"
RESOURCE_STATUS = "status"
commands = [EXIT, LIST_COFFEES, MAKE_COFFEE, REFILL, RESOURCE_STATUS, HELP]

# Coffee examples
ESPRESSO = "espresso"
AMERICANO = "americano"
CAPPUCCINO = "cappuccino"

lista_caf = [ESPRESSO, AMERICANO, CAPPUCCINO]

# Resources examples
WATER = "water"
COFFEE = "coffee"
MILK = "milk"

# Coffee maker's resources - the values represent the fill percents
res = {WATER: 2, COFFEE: 30, MILK: 100}

"""
Example result/interactions:

I'm a smart coffee maker
Enter command:
list
americano, cappuccino, espresso
Enter command:
status
water: 100%
coffee: 100%
milk: 100%
Enter command:
make
Which coffee?
espresso
Here's your espresso!
Enter command:
refill
Which resource? Type 'all' for refilling everything
water
water: 100%
coffee: 90%
milk: 100%
Enter command:
exit
"""

def refilling(a):
    
    if a.strip().lower() == "all":
            for i in res:
                    res[i] = 100
            printing(res)

    elif a.strip().lower() in res:
        res[a] = 100
        printing(res)

def find_equal_sign(text):
    return text.find('=')


def recipe_coff(coff):
    ok = True
    with open("recipes/" + str(coff) + ".txt", 'r') as f:
        for line in f:   #citire linie cu linie din fisier
            position = find_equal_sign(line)

            #atentie la primul rand (nu gaseste = si nu poate converti int()-ul)
            if position > 0:
                resursa = line[0:position]
                nr = int (line[position + 1 : len(line) -1])
                
                #verifica daca sunt destule resurse necesare disponibile
                if res[resursa] - nr < 0:
                    print("==== There are no available necessary resources. ====")
                    ok = False
                else:
                    res[resursa] -= nr
    if ok:

        #exista resurse disponibile => cafea realizata
        print("==== Here's your {}!====".format(coff))



def printing(res):

    #printarea tuturor resurselor
    for i in res:
            print("{}: {}%".format(i, res[i]))

print(" ==== I'm a simple coffee maker ==== ")
while(1):

    print("Enter command:")
    cuv = sys.stdin.readline()

    if(cuv.strip().lower() == "exit"):
        break


    elif(cuv.strip().lower() == "list"):
        for i in lista_caf:
            print(i)


    elif(cuv.strip().lower() == "status"):
        for i in res:
            print("{}: {}%".format(i, res[i]))


    elif(cuv.strip().lower() == "help"):
        print(" ==== How can i help you??? ====")


    elif(cuv.strip().lower() == "refill"):
        print("==== Which resource? Type 'all' for refilling everything ====")
        cuv = sys.stdin.readline().strip()
        if cuv.strip().lower() in res or cuv.strip().lower() == "all":
            refilling(cuv)
        else:
            print("==== There is no such filling. Try again! ====")
            continue

    
    elif(cuv.strip().lower() == "make"):
        print("==== Which coffee ???? ====")
        cuv = sys.stdin.readline().strip()
        if cuv in lista_caf:
            recipe_coff(cuv)
        else:
            continue
    
    else:
        print("==== There is no such command. Try again! ====")
        
