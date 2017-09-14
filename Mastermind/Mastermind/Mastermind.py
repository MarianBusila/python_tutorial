import random

def compute_solution(length, letter_count):
    possible_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:letter_count]
    print ("Possible letters: " + possible_letters)
    
    solution = ""
    for i in range(length):
        solution += random.choice(possible_letters)
    print ( "Solution: " + solution)
    return solution

def read_proposition(length):
    bValidInput = False
    while not bValidInput:
        user_input = input("Enter a string of  length " + str(length) + "> ")
        if len(user_input) == length:        
            print ("User input: " + user_input.upper())
            bValidInput = True
        else:
            print ("Invalid length. Please retry.")

    return user_input.upper()

def compute_rightmisplaced(proposition, solution):
    rights = 0
    misplaced = 0
    proposition_noright = ""
    solution_noright = ""

    for i, propchar in enumerate(proposition):
        if propchar == solution[i]:
            rights += 1
        else:
            proposition_noright += propchar
            solution_noright += solution[i]

    if rights == len(solution):
        return rights, misplaced
    
    for pn in proposition_noright:
        if pn in solution_noright:
            misplaced += 1
            solution_noright.replace(pn, "", 1)

    return rights, misplaced
        
def mastermind(length = 4, letter_count = 8):
    solution = compute_solution(length, letter_count)
    
    rights = 0
    while length != rights:
        proposition = read_proposition(length)
        rights, misplaced = compute_rightmisplaced(proposition, solution)
        print ("Rights: " + str(rights))
        print ("Misplaced: " + str(misplaced))


length = int ( input("Insert length: ") )
letter_count = int ( input("Insert letter_count: ") )
mastermind(length, letter_count)


    