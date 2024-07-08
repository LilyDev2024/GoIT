import random

def get_numbers_ticket(min, max, quantity):
    list_of_numbers = []

    if min < 1 or max > 1000 or quantity > (max - min + 1):
        #return list_of_numbers
        return []
    else: 
        list_of_numbers = (random.sample(range(min, max + 1), quantity))
        #return list_of_numbers.sort()
        list_of_numbers.sort()
        return list_of_numbers


print(get_numbers_ticket(1, 5, -3))