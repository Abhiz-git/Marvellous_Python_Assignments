def Pattern(no):
  
  for i in range(no):
    for j in range(no):
      print("*",end=" ")
    print()


def main():
  
  print("enter no: ",end=" ")
  a = int(input())
  Pattern(a)



if __name__ == "__main__":
  main()