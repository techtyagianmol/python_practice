input_num = int(input("Enter a number:-"))
if input_num < 0:
    print("the number cannot be negative")
else:
    factorial = 1
    num = input_num
    while input_num>0:
        factorial = factorial*input_num
        input_num=input_num-1

    print("factorial of ",num,"is",factorial)

