def betterinput(conditionsstr, message, errormessage):
    # Libraries import
    import os

    # Conditions list
    conditions = [conditionsstr[i:i+3].lower() for i in range(0, len(conditionsstr), 3)]
    
    # Error messages
    if len(conditionsstr) % 3 != 0: raise ValueError('BetterInput - Error: Invalid conditions added')
    if len(set(['int', 'flt', 'str']).intersection(conditions)) > 1: raise ValueError('BetterInput - Error: Two or more conflicting conditions')

    # Conditions program
    while True:
        try:
            if 'int' in conditions: inputans = int(input(message))
            if 'flt' in conditions: inputans = float(input(message))
            if 'str' in conditions: inputans = input(message)
            if 'cls' in conditions: os.system('cls')
            return inputans
        except: 
            if 'cls' in conditions: os.system('cls')
            print(errormessage)

