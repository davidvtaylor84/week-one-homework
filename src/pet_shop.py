# WRITE YOUR FUNCTIONS HERE

from locale import currency


def get_pet_shop_name(shop_name):
    return shop_name["name"]

def get_total_cash(cash):
    return cash["admin"]["total_cash"]

def add_or_remove_cash(total_cash, money):
    total_cash["admin"]["total_cash"] += money
    return total_cash
    
def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

def increase_pets_sold(pets_sold, increase_in_pet_sales):
    pets_sold["admin"]["pets_sold"] += increase_in_pet_sales
    return pets_sold

def get_stock_count(stock_count):
    return len(stock_count["pets"])

def get_pets_by_breed(number, breed):
    number = 0
    for pet in breed:
        total = len(breed["pets"]["breed"])
    number += len(breed["pets"]["breed"]) 
    return number

    # number = []
    # for breed in pets:
    #     breed = pets["pets"]["breed"]
    # number += breed
    # return number
    

# def find_no_friends(breed):
#     no_friend = []
#     for person in people:
#         if len(person["friends"])==0:
#             no_friend+=[person]
#     return no_friend