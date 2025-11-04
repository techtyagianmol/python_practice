numbers = [1,-1,2,-3,-4,5,6,-7,-8,9]

positive_number_count = 0
negative_number_count = 0

for num in numbers:
    if num > 0:
        positive_number_count += 1
    elif num < 0:
        negative_number_count += 1
print("final count of positive number is:- " , positive_number_count)
print("final count of negative number is:- " , negative_number_count)
