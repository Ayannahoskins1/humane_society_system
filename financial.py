class Transaction:
    def __init__(self, trans_id, description, amount, trans_type):
        self.trans_id = trans_id
        self.description = description
        self.amount = amount
        self.trans_type = trans_type  # "Donation", "Adoption Fee", "Expense"

    def __str__(self):
        return f"{self.trans_id}: {self.description} - {self.trans_type} - ${self.amount:.2f}"
