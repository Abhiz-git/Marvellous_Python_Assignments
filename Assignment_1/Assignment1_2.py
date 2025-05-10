def ChkNum(number):
    if (number % 2 == 0):
        return True
    
    return False


def main():
    print("Insert a number to check: ",end="")
    num = float(input())

    result = ChkNum(num) 
    if result:
        print("Even Number")
    else:
        print("Odd Number")


if __name__ == "__main__":
    main()