def Display(multiples):
    for i in range(multiples):
        print("Marvellous")


def main():
    print("Insert how many times to display: ",end="")
    num1 = int(input())

    Display(num1)


if __name__ == "__main__":
    main()