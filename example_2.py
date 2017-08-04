#
# CodeReboot 2017
# Example Program 2
#
# Skills Practiced
# - Basic Math & Operators
# - Control Flow Statements
# - User Input & Printing
#

from math import ceil

subtotal = 0.00
tax = 0.09
order_list = []


def order():
    global subtotal

    print("\nSubtotal: $" + str(subtotal))
    print("\nChoose an item from the menu:")
    print("1.) Burger $5.99")
    print("    Add Cheese $0.50")
    print("2.) Hot Dog $4.99")
    print("3.) Sandwich $3.99")
    print("4.) Fountain Drink $0.99")
    print("5.) View Order")
    print("6.) Finish Order")
    option = input("-> ")

    if option == "1":
        subtotal += 5.99

        print("\nAdded 1 Burger")
        print("Add cheese? [y / n]")
        option = input("-> ")

        if option == "y" or option == "Y" or option == "yes" or option == "Yes":
            subtotal += 0.50
            order_list.append("Hamburger w/ Cheese")

            print("\nAdded Cheese")
            order()
        else:
            order_list.append("Hamburger w/o Cheese")
            order()

    if option == "2":
        subtotal += 4.99
        order_list.append("Hot Dog")

        print("\nAdded 1 Hot Dog")
        order()

    if option == "3":
        subtotal += 3.99
        order_list.append("Sandwich")

        print("\nAdded 1 Sandwich")
        order()

    if option == "4":
        subtotal += 0.99
        order_list.append("Fountain Drink")

        print("\nAdded 1 Fountain Drink")
        order()

    if option == "5":
        print("\nItems you ordered:")

        if len(order_list) == 0:
            print("No items")
        else:
            for i in order_list:
                print("- " + i)

        print("\nEnter any key to go back:")
        option = input("-> ")
        order()

    if option == "6":
        pay()


def pay():
    total = ceil(((subtotal * tax) + subtotal) * 100) / 100.0
    print("\n" * 50)
    print("Subtotal: $" + str(subtotal))
    print("Tax: " + str(tax * 100) + "%")
    print("Total: $" + str(total))
    return


order()
