def Addition(First_number, Second_number):
    Add = 0
    Add = First_number + Second_number
    return Add


def main():
    print("Insert a First number: ",end="")
    num1 = float(input())

    print("Insert a Second number: ",end="")
    num2 = float(input())

    result = Addition(num1, num2) 

    print("Addition of 2 numbers is:",result)


if __name__ == "__main__":
    main()