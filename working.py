# Import required modules
from dataclasses import dataclass, asdict  # For creating simple data objects
from tabulate import tabulate              # For printing tables nicely in CLI
from datetime import datetime              # For date handling
import json                                # For reading/writing JSON file


# Dataclass representing one Expense entry
@dataclass
class Expense:
    id: int
    date: str
    description: str
    amount: float


# Load data from JSON file
# Returns a tuple: (unique_id, list_of_expenses)
def loadfile() -> tuple[int, list[Expense]]:
    with open('expense.json', 'r') as f:
        try:
            database = json.load(f)
        except Exception:
            # If file is empty or corrupted, return default values
            return (0, [])
    return (database[0], database[1])


# Save updated data back to JSON file
def savefile(unique_id, database):
    with open('expense.json', 'w') as f:
        try:
            json.dump([unique_id, database], f, indent=4)
        except Exception as e:
            print("Error: ", e)
            return False
    return True


class ExpenseTracker:

    # Add a new expense
    def addExpense(description, amount):
        unique_id, database = loadfile()

        # Increment ID for new expense
        unique_id = unique_id + 1

        try:
            # Validate amount type
            if not isinstance(amount, float):
                raise TypeError(
                    f"Amount must be numerical instead of {type(amount).__name__}"
                )

            description = str(description)
            amount = float(amount)

            # Create Expense object
            expense = Expense(
                unique_id,
                datetime.now().strftime("%d-%m-%Y"),
                description,
                amount
            )

            # Convert dataclass to dictionary before saving
            database.append(asdict(expense))

        except Exception as e:
            print("Error: ", e)

        # Save updated database
        if savefile(unique_id, database):
            return "Added Successfully"

    # Delete expense by ID
    def deleteExpense(id: int):
        unique_id, database = loadfile()

        # Filter out expense with matching ID
        database = [
            expense for expense in database
            if expense["id"] != id
        ]

        if savefile(unique_id, database):
            return "Deleted Successfully"

    # Get total expense summary
    # If month provided → calculate only that month's total
    def summary(month=None):
        database = loadfile()[1]
        total = 0

        if month is None:
            # Calculate total of all expenses
            for expense in database:
                total += expense["amount"]
            return total

        try:
            if isinstance(month, int):
                for expense in database:
                    expense_date = datetime.strptime(
                        expense["date"], "%d-%m-%Y"
                    )

                    # Match month and current year
                    if (
                        expense_date.month == month
                        and expense_date.year == datetime.now().year
                    ):
                        total += expense["amount"]
            else:
                raise TypeError(
                    f"Argument must be integer, not {type(month).__name__}"
                )

            return total

        except Exception as e:
            print("Error: ", e)

    # List all expenses
    # If month provided → filter by month
    def list(month=None):
        database = loadfile()[1]

        if month is None:
            # Print all expenses
            print(tabulate(database, tablefmt="rounded_outline"))
        else:
            try:
                if isinstance(month, int):
                    # Filter expenses by month and current year
                    database = [
                        expense for expense in database
                        if (
                            datetime.strptime(
                                expense["date"], "%d-%m-%Y"
                            ).month == month
                            and
                            datetime.strptime(
                                expense["date"], "%d-%m-%Y"
                            ).year == datetime.now().year
                        )
                    ]

                    print(tabulate(database, tablefmt="rounded_outline"))
                    return
                else:
                    raise TypeError(
                        f"Argument must be integer, not {type(month).__name__}"
                    )

            except Exception as e:
                print("Error: ", e)
