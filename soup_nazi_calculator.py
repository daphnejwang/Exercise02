import arithmetic

def soup_nazi_calculator():
    user_input = raw_input("Please provide what you'd like to calculate: ")
    parse_input = user_input.split(" ")
    list_length = len(parse_input)
    operator = parse_input[0]

    
    if operator == "q":
        quit()

    while True:
        try:
            num1 = int(parse_input[1])
            if list_length < 3:
                num2 = None
            elif list_length == 3:
                num2 = int(parse_input[2])
            elif list_length > 3:
                print "Sorry we only take up to 2 numbers"
                print "No calculator for you."
                quit()

            break
        except ValueError:
            print "That's not a number."
            print "No calculator for you."
            quit()

    if operator == "+":
        print arithmetic.add(num1,num2)
    elif operator == "-":
        print arithmetic.subtract(num1,num2)
    elif operator == "*":
        print arithmetic.multiply(num1,num2)
    elif operator == "/":
        print arithmetic.divide(num1,num2)
    elif operator == "square":
        print arithmetic.square(num1)
    elif operator == "cube":
        print arithmetic.cube(num1)
    elif operator == "pow":
        print arithmetic.power(num1,num2)
    elif operator == "mod":
        print arithmetic.mod(num1,num2)
    else:
        print "Sorry, we can't do that. The operators I take are +, -, *, /, square, cube, pow, mod, or q"

def main():
    while True:
        soup_nazi_calculator()

if __name__ == "__main__":
    main()