from datetime import datetime

employees = {
    "E101": {
        "Casual": 12,
        "Sick": 10,
        "Earned": 15
    }
}

def view_balance(emp_id):
    if emp_id not in employees:
        print("Employee ID not found.")
        return

    balance = employees[emp_id]

    print("\nLeave Balance:")
    print("Casual:", balance["Casual"])
    print("Sick:", balance["Sick"])
    print("Earned:", balance["Earned"])

def apply_leave():
    emp_id = input("Enter Employee ID: ").upper()

    if emp_id not in employees:
        print("Invalid Employee ID.")
        return

    leave_type = input("Enter Leave Type (Casual/Sick/Earned): ").capitalize()

    if leave_type not in employees[emp_id]:
        print("Invalid leave type.")
        return

    from_date = input("Enter From Date (YYYY-MM-DD): ")
    to_date = input("Enter To Date (YYYY-MM-DD): ")

    try:
        start = datetime.strptime(from_date, "%Y-%m-%d")
        end = datetime.strptime(to_date, "%Y-%m-%d")

    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # Check date order
    if end < start:
        print("Invalid dates. To-date cannot be before from-date.")
        return

    total_days = (end - start).days + 1

    balance = employees[emp_id][leave_type]

    if total_days <= balance:
        employees[emp_id][leave_type] -= total_days

        print(
            "Leave approved:", total_days,
            "days", leave_type,
            "| Balance", leave_type + ":",
            employees[emp_id][leave_type]
        )

    else:
        print(
            "Leave rejected. Requested:",
            total_days,
            "days | Available:",
            balance,
            "days"
        )

        print(
            "Casual:", employees[emp_id]["Casual"],
            "| Sick:", employees[emp_id]["Sick"],
            "| Earned:", employees[emp_id]["Earned"]
        )

def main():
    while True:
        print("\n===== Employee Leave Management System =====")
        print("1. Apply for Leave")
        print("2. View Leave Balance")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            apply_leave()

        elif choice == "2":
            emp_id = input("Enter Employee ID: ").upper()
            view_balance(emp_id)

        elif choice == "3":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
