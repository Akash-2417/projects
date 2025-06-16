
# users = {}  # Stores registered users by phone number
# bookings = []  # Stores food orders

# def create_account():
#     print("\n--- Create or Use Your Account ---")
#     name = input("Enter your name: ").strip()
#     phone = input("Enter your phone number: ").strip()

#     if phone in users:
#         print(f"👋 Welcome back, {users[phone]['name']}! You are eligible for 20% discount.")
#         discount = True
#     else:
#         users[phone] = {"name": name}
#         print(f"✅ Account created successfully! Hello, {name}.")
#         discount = False

#     return name, phone, discount

# def take_order(name, phone, discount):
#     print("\n--- Place Your Order ---")
#     food_name = input("Enter Food Name: ").strip()

#     while True:
#         try:
#             price = float(input("Enter Price: ₹"))
#             break
#         except ValueError:
#             print("Please enter a valid price (numbers only).")

#     while True:
#         portion = input("Half or Full?: ").strip().lower()
#         if portion in ['half', 'full']:
#             break
#         else:
#             print("Please enter 'Half' or 'Full'.")

#     while True:
#         try:
#             persons = int(input("Number of Persons: "))
#             break
#         except ValueError:
#             print("Please enter a valid number.")

#     if discount:
#         original_price = price
#         price = price * 0.8  # Apply 20% discount
#         print(f"🎉 20% discount applied! Original: ₹{original_price:.2f} → Now: ₹{price:.2f}")

#     order = {
#         "customer": name,
#         "phone": phone,
#         "food": food_name.title(),
#         "portion": portion.title(),
#         "price": round(price, 2),
#         "persons": persons
#     }

#     bookings.append(order)
#     print("✅ Order added successfully!")

# def view_bookings():
#     if not bookings:
#         print("No bookings yet.")
#         return

#     print("\n--- All Bookings ---")
#     for i, order in enumerate(bookings, start=1):
#         print(f"{i}. {order['customer']} - {order['food']} ({order['portion']}) - ₹{order['price']} - Persons: {order['persons']}")

# def main():
#     while True:
#         print("\n====== 🍽️ FOOD MENU BOOKING SYSTEM ======")
#         print("1. Create Account & Order")
#         print("2. View All Bookings")
#         print("3. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             name, phone, discount = create_account()
#             take_order(name, phone, discount)
#         elif choice == '2':
#             view_bookings()
#         elif choice == '3':
#             print("🙏 Thank for comming into our restaurnet..!")
#             break
#         else:
#             print("Invalid choice. Please select 1, 2, or 3.")

# if __name__ == "__main__":
#     main()


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error: Cannot perform modulus by zero."
    return x % y

def power(x, y):
    return x ** y

def main():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '7':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice. Please choose between 1 to 7.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", modulus(num1, num2))
        elif choice == '6':
            print("Result:", power(num1, num2))

if __name__ == "__main__":
    main()
