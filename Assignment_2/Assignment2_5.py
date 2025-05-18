
def Prime(no,a):
    if a == 2:
        print("Its Prime")
        return
    while(no>1):
        if a % no == 0:
            print("Its not a prime")
            return
        no = no-1
    print("Its is a prime")
    
def main():
    print("enter no: ",end=" ")
    a = int(input())
    no = a//2
    Prime(no,a)

if __name__ == "__main__":
    main()
  