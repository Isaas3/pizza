def start(order):
    subtotal = 0
    tax_rate = 0.095
    print("Customer Order:")
    for i in order:
        print(i.quantity, i.size, i.type, i.price)
        subtotal += i.quantity * i.price

    subtotal = round(subtotal, 2)
    tax = round(subtotal * tax_rate, 2)
    total = round(subtotal + tax, 2)

    print(f"Subtotal: ${subtotal}")
    print(f"Tax: ${tax}")
    print(f"Total: ${total}")

    payment(total)

    input("(Press ENTER to continue)")

def payment(total):
    while True:
        payment_type = input("Cash or credit? ")
        if payment_type.lower() == "cash":
            print(f"Your total is ${total}.")
            cash = int(input("Enter cash recieved: "))
            change = round(cash - total, 2)
            print(f"Return ${change} to the customer.")
            input("(Press ENTER to continue)")
            break
        elif payment_type.lower() == "credit":
            print(f"The total is ${total}.")
            print("Please swipe the credit card")
            input("(Press ENTER to continue)")
            break
        else:
            print("Please enter CASH or CREDIT only")