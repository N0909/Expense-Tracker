# Import ExpenseTracker class from working file
from working import ExpenseTracker

# Import argument parser for CLI
from argparse import ArgumentParser


def main():
    # Reference to ExpenseTracker class
    expense_tracker = ExpenseTracker

    # Create CLI parser
    parser = ArgumentParser(
        prog="expense-tracker",
        description="CLI tool to track expenses"
    )

    # Create subcommands (add, delete, list, summary)
    subparser = parser.add_subparsers(dest="command")

    # Add command
    add_expense = subparser.add_parser(
        name="add",
        help="Add a new expense"
    )
    add_expense.add_argument(
        "description",
        type=str,
        help="Expense Description"
    )
    add_expense.add_argument(
        "amount",
        type=float,
        help="Amount"
    )

    # Delete command
    remove_expense = subparser.add_parser(
        name="delete",
        help="Delete an expense"
    )
    remove_expense.add_argument(
        "id",
        type=int,
        help="ID of the expense"
    )

    # List command
    list_expense = subparser.add_parser(
        name="list",
        help="List expenses"
    )
    list_expense.add_argument(
        "--month",
        type=int,
        help="Month number"
    )

    # Summary command
    summary = subparser.add_parser(
        name="summary",
        help="Give total expense summary"
    )
    summary.add_argument(
        "--month",
        type=int,
        help="Month number"
    )

    # Parse CLI arguments
    args = parser.parse_args()

    # Handle commands
    if args.command == "add":
        print(
            expense_tracker.addExpense(
                args.description,
                args.amount
            )
        )

    elif args.command == "delete":
        print(
            expense_tracker.deleteExpense(
                args.id
            )
        )

    elif args.command == "list":
        expense_tracker.list(
            month=args.month if args.month else None
        )

    elif args.command == "summary":
        output = expense_tracker.summary(
            month=args.month if args.month else None
        )
        print("Total Expenses:", output)


# Run main only if file is executed directly
if __name__ == "__main__":
    main()
