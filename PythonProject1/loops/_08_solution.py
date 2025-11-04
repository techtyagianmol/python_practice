# check the number it is prime or not

number = int(input("Enter a number:->"))

is_prime = True

if number>1:
     for i in range(2,number):
         if number % i == 0:
             is_prime = False
             break


print("the number is prime or not:->", is_prime)

