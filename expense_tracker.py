
expenses = []

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Total\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount: "))
        expenses.append((name, amount))
    elif choice == "2":
        for i, (name, amount) in enumerate(expenses, 1):
            print(f"{i}. {name} - ₹{amount}")
    elif choice == "3":
        print(f"Total: ₹{sum(a for _, a in expenses)}")
    elif choice == "4":
        break
