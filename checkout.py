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
    save(order, total)

    input("(Press ENTER to continue)")

def payment(total):
    while True:
        payment_type = input("Cash or credit? ")
        if payment_type.lower() == "cash":
            print(f"Your total is ${total}.")
            cash = int(input("Enter cash recieved: "))
            change = round(cash - total, 2)
            print(f"Return ${change} to the customer.")
            break
        elif payment_type.lower() == "credit":
            print(f"The total is ${total}.")
            print("Please swipe the credit card")
            break
        else:
            print("Please enter CASH or CREDIT only")

def save(order, total):
    with open("pizza.dat", "a") as orders:
        for pizza in order:
            orders.write(f"{pizza.quantity}, {pizza.type}, {pizza.size}, {pizza.price} ")
        orders.write(f"{total}")
        orders.write("\n")