print("Select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    input1 = input("Enter the first number to add:")
    input2 = input("Enter the second number to add:")
    print("the sum of the first and second numbers", int(input1)+int(input2))
elif operation == "2":
            input1 = input("Enter the first number to subtract:")
            input2 = input("Enter the second number to subtract:")
            print("the sum of the first and second numbers", int(input1) - int(input2))
        
elif operation == "3":
            input1 = input("Enter the first number to multiply:")
            input2 = input("Enter the second number to multiply:")
            print(" the sum of the first and second numbers", int(input1)*int(input2))

elif operation == "4":
                input1  = input("Enter the first number to divide")
                input2  = input("Enter the second number to divide")
                print(" the sum of the first and second numbers", int(input1)/int(input2))
else: print("Invalid Entry")
