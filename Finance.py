class Transaction:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        print("Transaction added successfully.")

    def view_transactions(self):
        if self.transactions:
            for idx, transaction in enumerate(self.transactions, start=1):
                print(f"Transaction {idx}:")
                print(f"Date: {transaction.date}")
                print(f"Amount: ${transaction.amount}")
                print(f"Category: {transaction.category}")
                print(f"Description: {transaction.description}")
                print()
        else:
            print("No transactions found.")

    def calculate_total_expenses(self):
        total_expenses = sum(transaction.amount for transaction in self.transactions if transaction.amount < 0)
        print(f"Total expenses: ${-total_expenses}")

# Example usage:
if __name__ == "__main__":
    tracker = FinanceTracker()

    # Add transactions
    transaction1 = Transaction("2024-01-15", -50.00, "Groceries", "Weekly grocery shopping")
    transaction2 = Transaction("2024-01-18", -30.00, "Dining", "Dinner with friends")
    transaction3 = Transaction("2024-01-20", -100.00, "Utilities", "Electricity bill")
    tracker.add_transaction(transaction1)
    tracker.add_transaction(transaction2)
    tracker.add_transaction(transaction3)

    # View transactions
    print("Viewing all transactions:")
    tracker.view_transactions()

    # Calculate total expenses
    tracker.calculate_total_expenses()
