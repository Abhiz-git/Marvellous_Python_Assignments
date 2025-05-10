def main():

    print("Insert a number to check: ",end="")
    num = float(input())

    if num > 0:
        print("Positive Number")
    elif num < 0:
        print("Negative Number")
    else:
        print("Number is 0")

if __name__ == "__main__":
    main()