txt ="Press Enter after keying the required value."

print(txt)

num1 =float(input("Enter a number:"))
oper =input("Enter a operater:")
num2 =float(input("Enter an other number:"))

if oper =="+":
    print("Here is your answer:")
    print( num1+num2)
elif oper == "-":
    print("Here is your answer:")
    print( num1-num2)
elif oper == "/" :
    print("Here is your answer:")
    print(num1/num2)
elif oper == "x" :
    print("Here is your answer:")
    print( num1*num2)
elif oper == "X" :
    print("Here is your answer:")
    print( num1*num2)
elif oper == "*":
    print("Here is your answer:")
    print( num1*num2)
elif oper == "÷":
    print("Here is your answer:")
    print( num1/num2)
else:
        print("Invalid operator and you're a bitch for trying that😂")
        print("But well played 😂😂")

input("Press any key to exit")