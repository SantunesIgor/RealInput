class RealInput:
    def realinput(conditionsstr, message, errormessage):
        # Libraries import
        import os

        # Error messages
        if len(conditionsstr) % 3 != 0: print('RealInput - Error: Invalid conditions added')
        conditions = [conditionsstr[i:i+3].lower() for i in range(0, len(conditionsstr), 3)]

        # Conditions program
        if 'int' in conditions:
            while True:
                try: 
                    inputans = int(input(message))
                    if 'cls' in conditions: os.system('cls')
                    return inputans
                except: 
                    print(errormessage)
                    if 'cls' in conditions: os.system('cls')