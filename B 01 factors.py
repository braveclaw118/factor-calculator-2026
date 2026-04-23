# headings generator
def statement_generator(statement, decoration):
    print(f"\n {decoration * 5} {statement} {decoration * 5}")

# display instructions
def instructions():
    statement_generator("the epic factor finder", "-")
    print('''
say a number between 1 and 200
\n say xxx to break loop
some special numbers have special messages, like 1
    ''')
# get int between 1 and 200
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

# work out factors and return list
def factor(var_to_factor):
    factors_list = []

    # square root to figure out when looping stops
    stop = var_to_factor ** 0.5
    stop = int(stop)

    for item in range(1, stop + 1):

        # check to see if item is a factor
        if to_factor % item == 0:
            factors_list.append(item)

            # calculate partner
            partner = to_factor // item

            # Add partner to list without duplicates
            if partner not in factors_list:
                factors_list.append(partner)
    # return sorted list
    factors_list.sort()
    return factors_list
  


# Main routine

want_instructions = input("Press <Enter> to read instructions and any other key to continue")

if want_instructions == "":
    instructions()

while True:

    comment = ""

    # ask for number that is getting factorised
    to_factor = num_check("\nEnter an  integer or exit code")

    if to_factor == "xxx":
        break

    # get factors for integers >=2
    elif to_factor!= 1:
        all_factors = factor(to_factor)

    # Unity (by thefatrat)
    if to_factor == 1:
        all_factors = ""
        comment = "One is unity. Its only factor is itself"

    # square / prime comments

    # minos prime
    if len(all_factors) ==2:
        comment = f"{to_factor} is a prime number"

    # if square then why not square shaped
    elif len(all_factors) % 2 == 1:
        comment = f"{to_factor} is a perfect square"

    # wooo headings

    if to_factor >1:
        heading = f"factors of {to_factor}"
    else:
        heading = "One is special!"

    # final output
    print()
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)

# thanks for using our limited time imaginary friend remote! we hope you enjoy the next 2 days with your very own REAl, not so imaginary friend
print("Thanks for using the factors calculator!")