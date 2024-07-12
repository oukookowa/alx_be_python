#!/bin/bash
#Creates a shopping list manager with ability to delete, add, and view items on the list
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            # Prompt for and add an item
            while True:
                new_item = input("Enter the item to add: ")
                shopping_list.append(new_item)
                ans = input("Do you want to to add another item? Enter C to add new item or X to exit: ").upper
                if ans == "X":
                    print("Select another option from the menu...")
                    break
                else: 
                    ans == "C"
                    pass                       
        elif choice == '2':
            # Prompt to enter item to remove
            while True:
                item = input("Enter the item to remove: ")
                if item not in shopping_list:           
                    print("Item not found in shopping list!")
                    response = input("Do you want to to remove another item? Enter Y to continue or Q to exit: ").upper
                    if response == "Q":
                        print("Select another option from the menu...")
                        break
                    elif response not in ["Y", "Q"]:
                        print("Wrong input! Here's the menu once again...")
                        break
                    else:
                        response == "Y"
                        pass
                else:
                    shopping_list.remove(item)
                    feedback = input("Do you want to to remove another item? Enter P to continue or H to exit: ").upper
                    if feedback == "H":
                        print("Select another option from the menu...")
                        break
                    elif feedback not in ["P", "H"]:
                        print("Wrong input! Here's the menu once again...")
                        break
                    else:
                        response == "P"
                        pass    
        elif choice == '3':
            # Display the shopping list
            print(*shopping_list, sep = "\n")
            pass       
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            pass

if __name__ == "__main__":
    main()