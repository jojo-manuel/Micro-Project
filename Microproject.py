import tkinter as tk
from tkinter import messagebox

# Initialize grand total
grand_total = 0.0

# Function to add an item
def add_item():
    global grand_total  # Access the global grand total variable
    item = item_entry.get()
    try:
        qty = int(qty_entry.get())
        if qty < 0:
            messagebox.showerror("Error", "Invalid input! Please enter numeric values for quantity and price.")
            
        price = float(price_entry.get())
        if price < 0:
            messagebox.showerror("Error", "Invalid input! Please enter numeric values for quantity and price.")
        total = qty * price
        grand_total += total  # Update the grand total
        bill_list.insert(tk.END, f"{item}: {qty} x ₹{price:.2f} = ₹{total:.2f}")
        grand_total_label.config(text=f"Grand Total: ₹{grand_total:.2f}")  # Update grand total label
        item_entry.delete(0, tk.END)
        qty_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter numeric values for quantity and price.")

# Function to save the bill to a file
def save_output():
    bill_items = bill_list.get(0, tk.END)  # Get all items from the Listbox
    if bill_items:  # Check if the Listbox is not empty
        try:
            with open("output.txt", "w") as file:
                file.write("\n".join(bill_items))
                file.write(f"\n\nGrand Total: ₹{grand_total:.2f}")  # Save grand total to file
            messagebox.showinfo("Success", "Bill saved successfully as 'output.txt'!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving: {e}")
    else:
        messagebox.showwarning("Warning", "The bill is empty. Nothing to save!")

# Function to clear the bill
def clear_bill():
    global grand_total
    bill_list.delete(0, tk.END)
    grand_total = 0.0  # Reset grand total
    grand_total_label.config(text=f"Grand Total: ₹{grand_total:.2f}")  # Reset grand total label

# Main window
root = tk.Tk()
root.title("Simple Bill Generator")
root.geometry("400x600")

# Heading
heading = tk.Label(root, text="Bill Generator", font=("Arial", 18, "bold"), fg="Black")
heading.pack(pady=20)

# Input fields
tk.Label(root, text="Item Name:").pack()
item_entry = tk.Entry(root, width=30)
item_entry.pack()

tk.Label(root, text="Quantity:").pack()
qty_entry = tk.Entry(root, width=30)
qty_entry.pack()

tk.Label(root, text="Price per Unit:").pack()
price_entry = tk.Entry(root, width=30)
price_entry.pack()

# Buttons
tk.Button(root, text="Add Item", command=add_item).pack(pady=10)
tk.Button(root, text="Clear Bill", command=clear_bill).pack(pady=5)

save_button = tk.Button(root, text="Save Bill", command=save_output)
save_button.pack(pady=10)

# Bill display
bill_list = tk.Listbox(root, width=50, height=20)
bill_list.pack(pady=10)

# Grand total display
grand_total_label = tk.Label(root, text=f"Grand Total: ₹{grand_total:.2f}", font=("Arial", 14, "bold"), fg="green")
grand_total_label.pack(pady=10)

# Run the application
root.mainloop()
