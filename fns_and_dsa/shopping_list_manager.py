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
            new_item = input("Enter the item to add: ")
            shopping_list.append(new_item)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            if item not in shopping_list:           
                print("Item not found in shopping list!")
            else:
                shopping_list.remove(item)
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

if __name__ == "__main__":
    main()