"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45
SECONDS_PER_DAY = 24 * 60 * 60

# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    semester_cost = annual_cost/SEMESTERS_PER_YEAR
    return semester_cost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    month_cost = annual_cost/MONTHS_PER_YEAR
    return month_cost


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    day_cost = annual_cost/CLASS_DAYS_PER_SEMESTER/SEMESTERS_PER_YEAR
    return day_cost


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    credit_cost = annual_cost/credits/SEMESTERS_PER_YEAR
    return credit_cost


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    class_cost = cost_per_credit(annual_cost, credits)*CS1430_CREDITS/CS1430_MEETINGS_PER_SEMESTER
    return class_cost

def cost_per_second(annual_cost):
    """Give back what one second of the academic year costs."""
    second_cost = annual_cost/SECONDS_PER_DAY/CLASS_DAYS_PER_SEMESTER/SEMESTERS_PER_YEAR
    return second_cost

# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    annual_cost = float(input("Enter the total cost for one year: "))
    # Then ask for the credits this semester.
    credits = int(input("Enter the number of credits this semester: "))

    while True:
        print("per semester: 1")
        print("per month: 2")
        print("per day: 3")
        print("per credit: 4")
        print("per class: 5")
        print("per second: 6")
        print("Quit: Q")

        choice = input("Choose an option: ")

        if choice == "Q":
            break

        # Add a branch for each menu option here.
        if choice == "1":
            per_semester = cost_per_semester(annual_cost)
            print(f"Cost per semester: {per_semester:.2f}")
        elif choice == "2":
            per_month = cost_per_month(annual_cost)
            print(f"Cost per month: {per_month:.2f}")
        elif choice == "3":
            per_day = cost_per_day(annual_cost)
            print(f"Cost per day: {per_day:.2f}")
        elif choice == "4":
            per_credit = cost_per_credit(annual_cost, credits)
            print(f"Cost per credit: {per_credit:.2f}")
        elif choice == "5":
            per_class = cost_per_class(annual_cost, credits)
            print(f"Cost per class: {per_class:.2f}")
        elif choice == "6":
            per_second = cost_per_second(annual_cost)
            print(f"Cost per second: {per_second:.2f}")
        else:
            print("Invalid option. Please try again.")

# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
