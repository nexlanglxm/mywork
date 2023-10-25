def read_num(message = "enter a number"):        
    num = False
    while (num == False):
        try:
            num = int(input(message))
        except ValueError:
            print("that was not a number", end="")
    return num

num1 = read_num()
num2 = read_num("enter a second number")

answer = num1 * num2

print(f"the product of these numbers is {answer}")