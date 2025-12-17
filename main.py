import tkinter as tk
from tkinter import messagebox
from animal import Animal
from inventory import InventoryItem
from financial import Transaction

# -------------------- DATA STORAGE --------------------
animals = []
inventory = []
transactions = []

# -------------------- HUMAN-LOOKING SAMPLE DATA --------------------
# Animals
animals_data = [
    ("A001", "Buddy", "Dog", 3, "Healthy"),
    ("A002", "Mittens", "Cat", 2, "Healthy"),
    ("A003", "Charlie", "Dog", 5, "Needs vaccination"),
    ("A004", "Luna", "Cat", 1, "Healthy"),
    ("A005", "Max", "Dog", 4, "Healthy"),
    ("A006", "Bella", "Cat", 3, "Under observation"),
    ("A007", "Rocky", "Dog", 6, "Healthy"),
    ("A008", "Lucy", "Cat", 2, "Recovering"),
    ("A009", "Cooper", "Dog", 2, "Healthy"),
    ("A010", "Daisy", "Cat", 4, "Needs vaccination"),
    ("A011", "Toby", "Dog", 3, "Healthy"),
    ("A012", "Chloe", "Cat", 5, "Healthy"),
]

for data in animals_data:
    animal = Animal(*data)
    animals.append(animal)

# Pre-mark some as adopted
for a in animals[:6]:  # first 6 animals adopted
    a.mark_adopted()

# Inventory
inventory_data = [
    ("I001", "Dog Food - Chicken Flavor", 40, "kg", "Food"),
    ("I002", "Cat Food - Salmon Flavor", 35, "kg", "Food"),
    ("I003", "Dog Leash", 20, "pcs", "Supplies"),
    ("I004", "Cat Litter - Clumping", 15, "bags", "Supplies"),
    ("I005", "Vaccines - Canine Distemper", 12, "doses", "Medical"),
    ("I006", "Vaccines - Feline Rabies", 10, "doses", "Medical"),
    ("I007", "Dog Bedding", 8, "pcs", "Supplies"),
    ("I008", "Cat Toys", 25, "pcs", "Supplies"),
    ("I009", "Bandages", 30, "rolls", "Medical"),
    ("I010", "Treats - Mixed Flavors", 50, "packs", "Food"),
]

for data in inventory_data:
    item = InventoryItem(*data)
    inventory.append(item)

# Transactions
transactions_data = [
    ("T001", "Donation - John Smith", 150.0, "Donation"),
    ("T002", "Donation - Emily Carter", 200.0, "Donation"),
    ("T003", "Donation - Michael Lee", 100.0, "Donation"),
    ("T004", "Adoption Fee - Buddy", 75.0, "Adoption Fee"),
    ("T005", "Adoption Fee - Mittens", 50.0, "Adoption Fee"),
    ("T006", "Adoption Fee - Charlie", 65.0, "Adoption Fee"),
    ("T007", "Purchase - Dog Food - Chicken Flavor", 120.0, "Expense"),
    ("T008", "Purchase - Cat Food - Salmon Flavor", 90.0, "Expense"),
    ("T009", "Purchase - Vaccines - Canine Distemper", 60.0, "Expense"),
    ("T010", "Purchase - Cat Litter - Clumping", 45.0, "Expense"),
]

for data in transactions_data:
    trans = Transaction(*data)
    transactions.append(trans)

# -------------------- ANIMAL FUNCTIONS --------------------
def add_animal():
    def save():
        a_id = entry_id.get()
        name = entry_name.get()
        species = entry_species.get()
        age = entry_age.get()
        health = entry_health.get()
        animal = Animal(a_id, name, species, age, health)
        animals.append(animal)
        messagebox.showinfo("Success", f"Added {name}")
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Add Animal")

    tk.Label(add_window, text="ID:").grid(row=0, column=0)
    tk.Label(add_window, text="Name:").grid(row=1, column=0)
    tk.Label(add_window, text="Species:").grid(row=2, column=0)
    tk.Label(add_window, text="Age:").grid(row=3, column=0)
    tk.Label(add_window, text="Health:").grid(row=4, column=0)

    entry_id = tk.Entry(add_window)
    entry_name = tk.Entry(add_window)
    entry_species = tk.Entry(add_window)
    entry_age = tk.Entry(add_window)
    entry_health = tk.Entry(add_window)

    entry_id.grid(row=0, column=1)
    entry_name.grid(row=1, column=1)
    entry_species.grid(row=2, column=1)
    entry_age.grid(row=3, column=1)
    entry_health.grid(row=4, column=1)

    tk.Button(add_window, text="Save", command=save).grid(row=5, column=0, columnspan=2, pady=10)

def view_animals():
    view_window = tk.Toplevel(root)
    view_window.title("All Animals")
    for a in animals:
        tk.Label(view_window, text=str(a)).pack()

def mark_adopted():
    def adopt():
        selected_id = entry_id.get()
        found = False
        for a in animals:
            if a.animal_id == selected_id:
                a.mark_adopted()
                messagebox.showinfo("Success", f"{a.name} is now adopted!")
                adopt_window.destroy()
                found = True
                break
        if not found:
            messagebox.showerror("Error", "Animal ID not found.")

    adopt_window = tk.Toplevel(root)
    adopt_window.title("Mark Animal Adopted")

    tk.Label(adopt_window, text="Enter Animal ID to mark as adopted:").pack(pady=5)
    entry_id = tk.Entry(adopt_window)
    entry_id.pack(pady=5)

    tk.Button(adopt_window, text="Mark Adopted", command=adopt).pack(pady=10)

# -------------------- INVENTORY FUNCTIONS --------------------
def add_inventory():
    def save():
        i_id = entry_id.get()
        name = entry_name.get()
        quantity = entry_quantity.get()
        unit = entry_unit.get()
        category = entry_category.get()
        item = InventoryItem(i_id, name, int(quantity), unit, category)
        inventory.append(item)
        messagebox.showinfo("Success", f"Added {name}")
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Add Inventory Item")

    tk.Label(add_window, text="ID:").grid(row=0, column=0)
    tk.Label(add_window, text="Name:").grid(row=1, column=0)
    tk.Label(add_window, text="Quantity:").grid(row=2, column=0)
    tk.Label(add_window, text="Unit:").grid(row=3, column=0)
    tk.Label(add_window, text="Category:").grid(row=4, column=0)

    entry_id = tk.Entry(add_window)
    entry_name = tk.Entry(add_window)
    entry_quantity = tk.Entry(add_window)
    entry_unit = tk.Entry(add_window)
    entry_category = tk.Entry(add_window)

    entry_id.grid(row=0, column=1)
    entry_name.grid(row=1, column=1)
    entry_quantity.grid(row=2, column=1)
    entry_unit.grid(row=3, column=1)
    entry_category.grid(row=4, column=1)

    tk.Button(add_window, text="Save", command=save).grid(row=5, column=0, columnspan=2, pady=10)

def view_inventory():
    view_window = tk.Toplevel(root)
    view_window.title("Inventory")
    for item in inventory:
        tk.Label(view_window, text=str(item)).pack()

def update_inventory():
    def update():
        selected_id = entry_id.get()
        amount = int(entry_amount.get())
        found = False
        for item in inventory:
            if item.item_id == selected_id:
                item.update_quantity(amount)
                messagebox.showinfo("Success", f"{item.name} quantity updated to {item.quantity}")
                update_window.destroy()
                found = True
                break
        if not found:
            messagebox.showerror("Error", "Inventory ID not found.")

    update_window = tk.Toplevel(root)
    update_window.title("Update Inventory Quantity")

    tk.Label(update_window, text="Enter Inventory ID:").grid(row=0, column=0, pady=5)
    entry_id = tk.Entry(update_window)
    entry_id.grid(row=0, column=1, pady=5)

    tk.Label(update_window, text="Quantity to Add/Subtract:").grid(row=1, column=0, pady=5)
    entry_amount = tk.Entry(update_window)
    entry_amount.grid(row=1, column=1, pady=5)

    tk.Button(update_window, text="Update", command=update).grid(row=2, column=0, columnspan=2, pady=10)

# -------------------- FINANCIAL FUNCTIONS --------------------
def add_transaction():
    def save():
        t_id = entry_id.get()
        desc = entry_desc.get()
        amount = float(entry_amount.get())
        t_type = type_var.get()
        trans = Transaction(t_id, desc, amount, t_type)
        transactions.append(trans)
        messagebox.showinfo("Success", f"Added transaction: {desc}")
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Add Transaction")

    tk.Label(add_window, text="ID:").grid(row=0, column=0)
    tk.Label(add_window, text="Description:").grid(row=1, column=0)
    tk.Label(add_window, text="Amount:").grid(row=2, column=0)
    tk.Label(add_window, text="Type:").grid(row=3, column=0)

    entry_id = tk.Entry(add_window)
    entry_desc = tk.Entry(add_window)
    entry_amount = tk.Entry(add_window)
    type_var = tk.StringVar(add_window)
    type_var.set("Donation")
    type_menu = tk.OptionMenu(add_window, type_var, "Donation", "Adoption Fee", "Expense")

    entry_id.grid(row=0, column=1)
    entry_desc.grid(row=1, column=1)
    entry_amount.grid(row=2, column=1)
    type_menu.grid(row=3, column=1)

    tk.Button(add_window, text="Save", command=save).grid(row=4, column=0, columnspan=2, pady=10)

def view_transactions():
    view_window = tk.Toplevel(root)
    view_window.title("Transactions")
    for t in transactions:
        tk.Label(view_window, text=str(t)).pack()

# -------------------- SUMMARY REPORT --------------------
def summary_report():
    report_window = tk.Toplevel(root)
    report_window.title("Summary Report")
    report_text = tk.Text(report_window, width=80, height=30)
    report_text.pack(padx=10, pady=10)

    report_text.insert(tk.END, "===== Animals =====\n")
    if animals:
        for a in animals:
            report_text.insert(tk.END, str(a) + "\n")
    else:
        report_text.insert(tk.END, "No animals recorded.\n")

    report_text.insert(tk.END, "\n===== Inventory =====\n")
    if inventory:
        for item in inventory:
            report_text.insert(tk.END, str(item) + "\n")
    else:
        report_text.insert(tk.END, "No inventory recorded.\n")

    report_text.insert(tk.END, "\n===== Transactions =====\n")
    if transactions:
        for t in transactions:
            report_text.insert(tk.END, str(t) + "\n")
    else:
        report_text.insert(tk.END, "No transactions recorded.\n")

    report_text.config(state=tk.DISABLED)

# -------------------- MAIN WINDOW --------------------
root = tk.Tk()
root.title("Clay County Humane Society System")
root.geometry("600x800")

title = tk.Label(root, text="Clay County Humane Society", font=("Arial", 18, "bold"))
title.pack(pady=20)

subtitle = tk.Label(root, text="Shelter Management System", font=("Arial", 12))
subtitle.pack(pady=10)

# Buttons
tk.Button(root, text="Add Animal", command=add_animal, width=25, height=2).pack(pady=5)
tk.Button(root, text="View Animals", command=view_animals, width=25, height=2).pack(pady=5)
tk.Button(root, text="Mark Animal Adopted", command=mark_adopted, width=25, height=2).pack(pady=5)
tk.Button(root, text="Add Inventory", command=add_inventory, width=25, height=2).pack(pady=5)
tk.Button(root, text="View Inventory", command=view_inventory, width=25, height=2).pack(pady=5)
tk.Button(root, text="Update Inventory", command=update_inventory, width=25, height=2).pack(pady=5)
tk.Button(root, text="Add Transaction", command=add_transaction, width=25, height=2).pack(pady=5)
tk.Button(root, text="View Transactions", command=view_transactions, width=25, height=2).pack(pady=5)
tk.Button(root, text="View Summary Report", command=summary_report, width=25, height=2).pack(pady=5)

root.mainloop()
