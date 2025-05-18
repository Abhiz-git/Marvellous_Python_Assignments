Sum = 0

def Addition(no,a):
    global Sum
    if no>=1:
        if a % no == 0:
            Sum += no
        no = no-1
        Addition(no,a)
    return Sum


def main():
    print("enter no: ",end=" ")
    a = int(input())
    no = a//2
    print(Addition(no,a))

if __name__ == "__main__":
    main()
  