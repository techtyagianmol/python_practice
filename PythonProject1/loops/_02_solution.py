number = int(input("Enter a number:"))

sum_even = 0

for i in range(1,number+1):
    if i%2 ==0:
        sum_even += i
print(str(sum_even),"is a sum of even numbers in the list of numbers to n number")


