import calendar
import tkinter as tk
from tkinter import messagebox

# Function to display calendar using CLI
def display_calendar_cli():
    year = int(input("Enter a Valid Year: "))
    month = int(input("Enter a Valid month (1 - 12): "))
    
    print(calendar.month(year, month))

# Function to display calendar using GUI
def display_calendar_gui():
    # Create the GUI window
    root = tk.Tk()
    root.title("Calendar Display")
    
    # Create labels and entry fields for year and month
    year_label = tk.Label(root, text="Enter Year:")
    year_label.pack()
    year_entry = tk.Entry(root)
    year_entry.pack()
    
    month_label = tk.Label(root, text="Enter Month (1 - 12):")
    month_label.pack()
    month_entry = tk.Entry(root)
    month_entry.pack()
    
    # Function to display calendar based on user input
    def display_calendar():
        year = int(year_entry.get())
        month = int(month_entry.get())
        
        if 1 <= month <= 12:
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, calendar.month(year, month))
        else:
            # Show an error message using tkinter messagebox
            messagebox.showerror("Invalid Input", "Please enter a valid month (1 - 12).")
    
    # Create a button to trigger calendar display
    display_button = tk.Button(root, text="Display Calendar", command=display_calendar)
    display_button.pack()
    
    # Create a text widget to display the calendar
    result_text = tk.Text(root, height=10, width=25)
    result_text.pack()
    
    # Start the GUI event loop
    root.mainloop()

# Ask the user for their choice
while True:
    choice = input("Do you want to see the calendar using CLI or GUI? (cli/gui/exit): ").lower()
    
    if choice == "cli":
        display_calendar_cli()
    elif choice == "gui":
        display_calendar_gui()
    elif choice == "exit":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 'cli', 'gui', or 'exit'.")
