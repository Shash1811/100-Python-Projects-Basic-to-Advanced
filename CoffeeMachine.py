served = True
resources = {'Water':1000,'Milk':1000,'Coffee':1000,'Money':0.0}
def report():
    print(f"Water:{resources['Water']}ml")
    print(f"Milk:{resources['Milk']}ml")
    print(f"Coffee:{resources['Coffee']}g")
    print(f"Money:{resources['Money']}$")
def check_resources(order):
    if order.lower() == 'expresso':
        if resources['Water']<50:
            print("Sorry not enough water")
            return False
        elif resources['Coffee']<18:
            print("Sorry not enough Coffee")
            return False
    if order.lower() == 'latte':
        if resources['Water']<200:
            print("Sorry not enough water")
            return False
        elif resources['Coffee']<24:
            print("Sorry not enough Coffee")
            return False
        elif resources['Milk']<150:
            print("Sorry not enough Milk")
            return False
    if order.lower() == 'cappuccino':
        if resources['Water'] < 250:
            print("Sorry not enough water")
            return False
        elif resources['Coffee'] < 24:
            print("Sorry not enough Coffee")
            return False
        elif resources['Milk'] < 100:
            print("Sorry not enough Milk")
            return False
        return True
def sufficient(order,money):
    if order.lower() == "expresso":
        cost = 1.50
    elif order.lower() == "latte":
        cost = 2.50
    elif order.lower() == "cappuccino":
        cost = 3.00
    if(cost==money):
        return True
    return False
def deduct(order):
    if order.lower() == "expresso":
        resources['Water']-=50
        resources['Coffeee']-=18
    elif order.lower() == "latte":
        resources['Water']-=200
        resources['Coffee']-=24
        resources['Milk']-=150
    elif order.lower() == "cappuccino":
        resources['Water']-=250
        resources['Coffee']-=24
        resources['Milk']-=100
def excess(order,money):
    if order.lower() == "expresso":
        cost = 1.50
    elif order.lower() == "latte":
        cost = 2.50
    elif order.lower() == "cappuccino":
        cost = 3.00
    if (money>cost):
        return True
    return False
def change_amt(order,money):
    if order.lower() == "expresso":
        cost = 1.50
    elif order.lower() == "latte":
        cost = 2.50
    elif order.lower() == "cappuccino":
        cost = 3.00
    return money-cost
while served==True:
    order = input("What would you like? (espresso/latte/cappuccino):")
    if order == "off":
        exit()
    elif order == "report":
        report()
        
    if not check_resources(order):
        continue
    else:
        penny = float(input("Enter the number of pennies:"))
        nickel = float(input("Enter the number of nickels:"))
        dime = float(input("Enter the number of dimes:"))
        quarter = float(input("Enter the number of quarters:"))
        money = penny*0.01+nickel*0.05+dime*0.10+quarter*0.25

        if excess(order, money):
            deduct(order)
            change = change_amt(order,money)
            print(f"Here's your {order}.Enjoy!")
            print(f"Here's your {change}")
            resources['Money']+=(money-change)
        elif sufficient(order,money):
            deduct(order)
            resources['Money'] += money
            deduct(order)
            print(f"Here's your {order}.Enjoy!")

        else:
            print("Sorry not enough Money!Money refunded")







