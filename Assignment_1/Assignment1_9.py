def main():
    cnt = 0
    num = 0
    while (cnt < 10):
        num += 1
        if num % 2 == 0:
            print(num,"",end="")
            cnt +=1

if __name__ == "__main__":
    main()