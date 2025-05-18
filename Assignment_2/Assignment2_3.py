Fact = 1

def Factorial(no):
    global Fact
    if no>=1:
        Fact *= no
        no = no-1
        Factorial(no)
    return Fact


def main():
    print("enter no: ",end=" ")
    a = int(input())

    print(Factorial(a))

if __name__ == "__main__":
    main()
  