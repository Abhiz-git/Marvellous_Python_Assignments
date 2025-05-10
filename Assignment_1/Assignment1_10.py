def lenX(Name):
    cnt = 0
    for i in Name:
        cnt += 1
    
    return cnt

def main():
    
    print("Insert a Name or string whose length to count: ",end="")
    String = input()
    Length = lenX(String)
    print(Length)

if __name__ == "__main__":
    main()