print("welcome to the gussing game")
print("to close the game enter X")

while True:
    n=input("enter the number :")
    if n=="x":
        print("close the game")
        print('thanks')
        break
    try:
        n=int(n)
        if n%2==0:
            print("this number is even")
        else:
                print("this number is odd")
    except ValueError:
        print("please,Enter a valid number")
        print("-----------------------------")
        

