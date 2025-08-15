Menu = {
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee": 18,
        },
        "cost": 50,
    },
    "latte":{
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 80,
    },
    "cappuccino":{
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 100,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

while True:

    print("\n--------Coffee Menu--------")
    for coffee_name in Menu:
        print(f"{coffee_name.capitalize()} : ₹{Menu[coffee_name]['cost']}")

    choice=input("\nWhat would you like to have? (espresso/latte/cappuccino)\nType 'report' to see stock or 'no' to exit:").lower()

    if choice == 'report':
        for key in resources:
            print(f"{key} : {resources[key]}")
        continue
    
    
    elif choice == 'no':
        break
    

    elif choice in Menu:

        enough_stock=True
        for item in Menu[choice]["ingredients"]:
            if Menu[choice]["ingredients"][item] > resources[item]:
                print(f"Sorry, There is not enough {item}")
                enough_stock =False
                break
        if not enough_stock:
                continue

        print("\nPlease Insert Coins")
        ten_rupee = 10 * int(input("How many ₹10 coins:"))
        five_rupee = 5 * int(input("How many ₹5 coins: "))
        two_rupee = 2 * int(input("How many ₹2 coins: "))
        one_rupee = 1 * int(input("How many ₹1 coins: "))


        user_total_amount = ten_rupee + five_rupee + two_rupee + one_rupee

        if user_total_amount < Menu[choice]['cost']:
            print(f"Insufficient Amount! Refunding ₹{user_total_amount}")
            continue

        change = user_total_amount - Menu[choice]['cost']
        if change > 0:
            print(f"Here is your change ₹{change}")
            
        resources['money'] += Menu[choice]['cost']

        for item in Menu[choice]['ingredients']:
            resources[item] -= Menu[choice]['ingredients'][item]
            
        print(f"Here is your {choice}. Enjoy!")
    
    else:
        print("Invalid Option, Choose Again!")
print("Thanks for using our Coffee Machine! Have a nice day")