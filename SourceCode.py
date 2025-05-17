# Small-Scale ERP System

# Libraries for better visualization
import os

# Inventory, Sales, and Employee Data (Mock Database)
inventory = []
sales = []
employees = []


# Function to clear console (optional for clarity)
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# 1. Inventory Management
def add_inventory_item():
    clear_console()
    item_name = input("Enter item name: ")
    quantity = int(input("Enter item quantity: "))
    price = float(input("Enter item price: "))
    inventory.append({"name": item_name, "quantity": quantity, "price": price})
    print("Item added successfully!")


def view_inventory():
    clear_console()
    print("Inventory:")
    for item in inventory:
        print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}")
    input("\nPress Enter to continue...")


def update_inventory():
    clear_console()
    item_name = input("Enter item name to update: ")
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            item["quantity"] = int(input("Enter new quantity: "))
            item["price"] = float(input("Enter new price: "))
            print("Item updated successfully!")
            return
    print("Item not found!")


# 2. Sales Management
def record_sale():
    clear_console()
    item_name = input("Enter sold item name: ")
    quantity_sold = int(input("Enter quantity sold: "))
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            if item["quantity"] >= quantity_sold:
                item["quantity"] -= quantity_sold
                total_price = quantity_sold * item["price"]
                sales.append({"item": item_name, "quantity": quantity_sold, "total_price": total_price})
                print(f"Sale recorded! Total Price: {total_price}")
                return
            else:
                print("Insufficient quantity in inventory!")
                return
    print("Item not found in inventory!")


def view_sales():
    clear_console()
    print("Sales:")
    total_sales = 0
    for sale in sales:
        print(f"Item: {sale['item']}, Quantity: {sale['quantity']}, Total Price: {sale['total_price']}")
        total_sales += sale["total_price"]
    print(f"\nTotal Sales Amount: {total_sales}")
    input("\nPress Enter to continue...")


# 3. Employee Management
def add_employee():
    clear_console()
    emp_name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    department = input("Enter employee department: ")
    employees.append({"name": emp_name, "id": emp_id, "department": department})
    print("Employee added successfully!")


def view_employees():
    clear_console()
    print("Employees:")
    for emp in employees:
        print(f"Name: {emp['name']}, ID: {emp['id']}, Department: {emp['department']}")
    input("\nPress Enter to continue...")


# Main Menu
def main_menu():
    while True:
        clear_console()
        print("Small-Scale ERP System")
        print("1. Inventory Management")
        print("2. Sales Management")
        print("3. Employee Management")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            inventory_menu()
        elif choice == "2":
            sales_menu()
        elif choice == "3":
            employee_menu()
        elif choice == "4":
            print("Exiting ERP System. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")


# Sub-Menus
def inventory_menu():
    while True:
        clear_console()
        print("Inventory Management")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_inventory_item()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            update_inventory()
        elif choice == "4":
            break
        else:
            print("Invalid choice! Try again.")


def sales_menu():
    while True:
        clear_console()
        print("Sales Management")
        print("1. Record Sale")
        print("2. View Sales")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            record_sale()
        elif choice == "2":
            view_sales()
        elif choice == "3":
            break
        else:
            print("Invalid choice! Try again.")


def employee_menu():
    while True:
        clear_console()
        print("Employee Management")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            break
        else:
            print("Invalid choice! Try again.")


# Run the ERP System
if __name__ == "__main__":
    main_menu()
