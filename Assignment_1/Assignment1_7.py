def Divisiblity(number):
    if (number % 5 == 0):
        return True
    
    return False


def main():
    print("Insert a number to check: ",end="")
    num = float(input())

    result = Divisiblity(num) 
    print(result)


if __name__ == "__main__":
    main()