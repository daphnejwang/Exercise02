import arithmetic

def get_user_input():
    user_input = raw_input("Please provide what you'd like to calculate: ")
    parse_input = user_input.split(" ")
    
    operator = parse_input[0]
    if operator == "q":
        quit()

    num1 = int(parse_input[1])

    if operator == "square" or operator == "cube":
        num2 = None
    else:
        num2 = int(parse_input[2])


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
        print "Sorry, we can't do that."

def main():
    while True:
        get_user_input()

if __name__ == "__main__":
    main()