def Display1(num):
    print("printing using one way\n")

    print("* "*num)

def Display2(num):
    print("printing using loop way")

    for i in range(num):
        print("*\t",end="")

def main():

    print("Insert a count of stars to print: ",end="")
    num = int(input())

    Display1(num)
    Display2(num)
    
    
if __name__ == "__main__":
    main()