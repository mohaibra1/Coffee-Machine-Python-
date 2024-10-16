import math

# Write your code here
def make_coffee():
    print('''Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
    ''')
money = 550
water = 400
milk = 540
beans = 120
d_cup = 9



def ingredients_calculator(c, w, m, b):
    w_ratio = math.floor(w/200)
    m_ratio = math.floor(m/50)
    b_ratio = math.floor(b/15)
    lis = [w_ratio, m_ratio, b_ratio]
    amount = min(lis)
    remaining = c - amount
    if amount == c:
        print('Yes, I can make that amount of coffee')
    elif remaining < 0:
        print(f'Yes, I can make that amount of coffee (and even {abs(remaining)} more than that)')
    elif remaining >= 0:
        print(f'No, I can make only {amount} cups of coffee')


def can_make_coffee():
    print('Write how many ml of water the coffee machine has:')
    w = int(input())
    print('Write how many ml of milk the coffee machine has:')
    m = int(input())
    print('Write how many grams of coffee beans the coffee machine has:')
    b = int(input())
    print('Write how many cups of coffee you will need:')
    cups = int(input())
    ingredients_calculator(cups, w, m, b)
def espresso():
    global water, money, d_cup, beans
    if water < 250:
        print("Sorry, not enough water!")
        return
    elif d_cup < 1:
        print(f"Sorry, not enough cups!")
        return
    elif beans < 16:
        print(f"Sorry, not enough coffee beans!")
        return
    else:
        print('I have enough resources, making you a coffee!')
    w = 250 * 1
    b = 16 * 1
    d_cup -= 1
    water -= w
    beans -= b
    money += 4

def latte():
    global water, money, d_cup, beans, milk
    if water < 350:
        print("Sorry, not enough water!")
        return
    elif milk < 75:
        print("Sorry, not enough milk!")
        return
    elif d_cup < 1:
        print(f"Sorry, not enough cups!")
        return
    elif beans < 20:
        print(f"Sorry, not enough coffee beans!")
        return
    else:
        print('I have enough resources, making you a coffee!')
    w = 350 * 1
    m = 75 * 1
    b = 20 * 1
    d_cup -= 1
    water -= w
    milk -= m
    beans -= b
    money += 7
def cappuccino():
    global water, money, d_cup, beans, milk
    if water < 200:
        print("Sorry, not enough water!")
        return
    elif milk < 100:
        print("Sorry, not enough milk!")
        return
    elif d_cup < 1:
        print(f"Sorry, not enough cups!")
        return
    elif beans < 12:
        print(f"Sorry, not enough coffee beans!")
        return
    else:
        print('I have enough resources, making you a coffee!')
    w = 200 * 1
    m = 100
    b = 12 * 1
    d_cup -= 1
    water -= w
    milk -= m
    beans -= b
    money += 6

def buy():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
    choice = input()
    if choice == '1':
        espresso()
    elif choice == '2':
        latte()
    elif choice == '3':
        cappuccino()
    elif choice == 'back':
        return
    else:
        print('Wrong input!')

def fill():
    global water, milk, beans, d_cup
    print('Write how many ml of water you want to add:')
    w = int(input())
    water += w
    print('Write how many ml of milk you want to add: ')
    m = int(input())
    milk += m
    print('Write how many grams of coffee beans you want to add:')
    b = int(input())
    beans += b
    print('Write how many disposable cups you want to add:')
    c = int(input())
    d_cup += c

def take():
    global money
    print(f'I gave you ${money}')
    money = 0

def coffee_machine():
    stop = True
    while stop:
        print('Write action (buy, fill, take, remaining, exit): ')
        action = input()

        if action == 'buy':
            print()
            buy()
        elif action == 'fill':
            print()
            fill()
        elif action == 'take':
            print()
            take()
        elif action == 'exit':
            print()
            stop = False
        elif action == 'remaining':
            print()
            print('The coffee machine has:')
            print(f'{water} ml of water')
            print(f'{milk} ml of milk')
            print(f'{beans} g of coffee beans')
            print(f'{d_cup} disposable cups')
            print(f'${money} of money')
        print()
coffee_machine()