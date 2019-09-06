from acme import Product
import random

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products: int = 30):
    prod_list = []
    
    for _ in range(30):
        name1 = random.choice(ADJECTIVES)
        name2 = random.choice(NOUNS)
        name = name1 + ' ' + name2
        price = random.randint(5,100)
        weight = random.randint(5,100)
        flammability = random.uniform(0.0,2.5)

        newProd = Product(name,price,weight,flammability)
        prod_list.append(newProd)
    
    return prod_list

def inventory_report(prod_list: list):
    unique_names = []
    prices = []
    weights = []
    flammabilities = []
    
    for prod in prod_list:
        if prod.name not in unique_names:
            unique_names.append(prod.name)
        
        prices.append(prod.price)
        weights.append(prod.weight)
        flammabilities.append(prod.flammability)
    
    num_unique_names = len(unique_names)
    avg_price = sum(prices)/len(prices)
    avg_weight = sum(weights)/len(weights)
    avg_flammability = sum(flammabilities)/len(flammabilities)

    print('Number of unique names: ', num_unique_names)
    print('Avg price: ', avg_price)
    print('Avg weight: ', avg_weight)
    print('Avg flammability: ', avg_flammability)

    
if __name__ == '__main__':
    inventory_report(generate_products())

