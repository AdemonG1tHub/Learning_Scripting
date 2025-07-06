# Simple Checkout
# Scripted by Adem U and BendieGames
# 06/07/25 (UK date format)

# Note: Currently only allows for 1 item to be purchased. Will work on a way to purchase multiple tomorrow.

# Firstly, define our items and prices.tt
import os
item1 = "Auction House"
item1Price = "$30"
item2 = "Shop System"
item2Price = "$20"
item3 = "Ban System"
item3Price = "$5"
item4 = "Discord Relay"
item4Price = "$50"

checkout_basket = []
validAnswer = False

# Display available items
print(f"Here is what we have to offer:\n1. {item1}\n2. {item2}\n3. {item3}\n4. {item4}")

# Get user item selection
def checkout():
    _ = os.system('cls')
    print(f"Here is what we have to offer:\n1. {item1}\n2. {item2}\n3. {item3}\n4. {item4}")
    answer = input("\nIf you'd like to order any of these, type the number of the first item you'd like to purchase, however if you want to complete your purchases then enter EXIT: ")

    if answer == "1":
        print("Item 1 selected.")
        checkout_basket.append(f"\nYour basket has {item1} and costs {item1Price}")
        checkout()
    elif answer == "2":
        print("Item 2 added to basket.")
        checkout_basket.append(f"\nYou added {item2} to your basket and it costs {item2Price}")
        checkout()
    elif answer == "3":
        print("Item 3 selected.")
        checkout_basket.append(f"\nYour basket has {item3} and costs {item3Price}")
        checkout()
    elif answer == "4":
        print("Item 4 selected.")
        checkout_basket.append(f"\nYour basket has {item4} and costs {item4Price}")
        checkout()
    elif answer == "EXIT":
        print("Your current basket: ")
        for item in checkout_basket:
            print(item)
        global validAnswer
        while not validAnswer:
            confirmation = input("\nWould you like to go ahead with this transaction? (Y/N): ").strip().upper()
            if confirmation == "Y":
                print("Done! Your payment has been received!")
                validAnswer = True
            elif confirmation == "N":
                print("Payment cancelled.")
                validAnswer = True
            else:
                print("Invalid answer. Please type Y or N.\n")
    else:
        print("Invalid selection.")
        checkout()

checkout()

