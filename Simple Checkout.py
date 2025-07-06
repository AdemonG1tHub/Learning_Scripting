# Simple Checkout
# Scripted by Adem U
# 06/07/25 (UK date format)

# Note: Currently only allows for 1 item to be purchased. Will work on a way to purchase multiple tomorrow.

# Firstly, define our items and prices.tt
item1 = "Auction House"
item1Price = "$30"
item2 = "Shop System"
item2Price = "$20"
item3 = "Ban System"
item3Price = "$5"

checkoutCompleted = False
validAnswer = False
checkout = ""

# Display available items
print(f"Here is what we have to offer:\n1. {item1}\n2. {item2}\n3. {item3}")

# Get user item selection
while not checkoutCompleted:
    answer = input("\nIf you'd like to order any of these, type the number of the first item you'd like to purchase: ")

    if answer == "1":
        print("Item 1 selected.")
        checkout = f"\nYour basket has {item1} and costs {item1Price}"
        checkoutCompleted = True
    elif answer == "2":
        print("Item 2 selected.")
        checkout = f"\nYour basket has {item2} and costs {item2Price}"
        checkoutCompleted = True
    elif answer == "3":
        print("Item 3 selected.")
        checkout = f"\nYour basket has {item3} and costs {item3Price}"
        checkoutCompleted = True
    else:
        print("Invalid selection.")

print(checkout)

# Get user confirmation
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
