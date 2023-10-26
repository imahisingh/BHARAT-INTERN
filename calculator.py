import tkinter as tk

# Function to perform calculations
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operator.get()

        if operation == "Add":
            result.set(num1 + num2)
        elif operation == "Subtract":
            result.set(num1 - num2)
        elif operation == "Multiply":
            result.set(num1 * num2)
        elif operation == "Divide":
            if num2 == 0:
                result.set("Cannot divide by zero")
            else:
                result.set(num1 / num2)
    except ValueError:
        result.set("Invalid input")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Entry fields for numbers
entry_num1 = tk.Entry(window)
entry_num2 = tk.Entry(window)

# Label to display the result
result = tk.StringVar()
result.set("Result: ")

result_label = tk.Label(window, textvariable=result)

# Dropdown menu for operations
operator = tk.StringVar()
operator.set("Add")

operator_menu = tk.OptionMenu(window, operator, "Add", "Subtract", "Multiply", "Divide")

# Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)

# Packing the GUI elements
entry_num1.pack()
entry_num2.pack()
operator_menu.pack()
calculate_button.pack()
result_label.pack()

# Start the main GUI loop
window.mainloop()
