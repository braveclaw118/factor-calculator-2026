# Generates headings
def statement_generator(statement, decoration):
    print(f"\n {decoration * 5} {statement} {decoration * 5}")

# Display instructions
def instructions():
    statement_generator("teh epic factor finder", "-")
    print('''
say a number between 1 and 200
\n say xxx to break loop
    ''')


#ask for width and loop until they enter a number that's more than 0

def num_check(question):

    error = "Please enter an integer that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response
        try:
            # ask user for number
            response = int(response)
            # check number is between 1 and 200
            if 1 <= response <=  200:
                return response
            else:(print(error))
        except ValueError:
            print (error)

# main routine goes here


# display instructions
want_instructions = input("Press <Enter> to read instructions and any other key to continue")

if want_instructions == "":
    instructions()

while True:
    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)
    if to_factor == "xxx":
        break