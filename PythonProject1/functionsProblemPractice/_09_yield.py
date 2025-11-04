limit = int(input("enter the limit here:-"))


def even_generator(limit):
    for i in range(0,limit+1,2):
        yield i


for num in even_generator(limit):
    print(num)