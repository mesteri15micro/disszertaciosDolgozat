import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import time
import sys


# Function to handle button click
def handle_click():
    # Get user selections
    selected_task = task_var.get()
    input_file = file_var.get()
    output_location = output_var.get()
    running_time = time_var.get()

    # Perform actions based on user selections
    # Placeholder code, replace with actual logic
    print("Selected Task:", selected_task)
    print("Input File:", input_file)
    print("Output Location:", output_location)
    print("Running Time:", running_time)

# Function to exit the program
def exit_program():
    window.destroy()
    #sys.exit()

# Function to exit the application
def exit_app():
    window.quit()

# Create the main window
window = tk.Tk()
window.title("Customized User Interface")
window.geometry("400x600")

# Option 1: Choose NP complete task
task_label = tk.Label(window, text="Choose NP complete task:")
task_label.pack()
task_var = tk.StringVar(window)
task_var.set("Binpacking")  # Set default task
task_dropdown = tk.OptionMenu(window, task_var, "Binpacking (descending)", "Binpacking (ascending)",
                              "Binpacking (random order)", "Knapsack", "Graph coloring",
                              "Hamilton circle problem", "Cristophides algorithm")
task_dropdown.pack()

# Option 2: Select input data files
file_label = tk.Label(window, text="Select input data file:")
file_label.pack()
file_var = tk.StringVar(window)
file_button = tk.Button(window, text="Browse", command=lambda: file_var.set(filedialog.askopenfilename()))
file_entry = tk.Entry(window, textvariable=file_var, state="readonly")
file_button.pack()
file_entry.pack()

# Option 3: Choose output data location
output_label = tk.Label(window, text="Choose output data location:")
output_label.pack()
output_var = tk.StringVar(window)
output_button = tk.Button(window, text="Browse", command=lambda: output_var.set(filedialog.askdirectory()))
output_entry = tk.Entry(window, textvariable=output_var, state="readonly")
output_button.pack()
output_entry.pack()

# Option 4: Enter running time
time_label = tk.Label(window, text="Enter running time (HH:MM:SS):")
time_label.pack()
time_var = tk.StringVar(window)
time_entry = tk.Entry(window, textvariable=time_var)
time_entry.pack()

# Option 5: Display progress bar
progress_label = tk.Label(window, text="Progress:")
progress_label.pack()
#progress_bar = tk.ttk.Progressbar(window, length=200, mode="determinate")
progress_bar = ttk.Progressbar(window, length=200, mode="determinate")
progress_bar.pack()

# Option 6: Display running time and date
time_date_label = tk.Label(window, text="Running Time / Date:")
time_date_label.pack()
time_date_var = tk.StringVar(window)
time_date_label = tk.Label(window, textvariable=time_date_var)
time_date_label.pack()

# Button to start the program
start_button = tk.Button(window, text="Start", command=handle_click)
start_button.pack()

# Button to exit the application
exit_button = tk.Button(window, text="Exit", command=exit_program)
exit_button.pack()

# Update the running time and date continuously
def update_time_date():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%Y-%m-%d")
    time_date_var.set(current_time + " / " + current_date)
    window.after(1000, update_time_date)

# Start updating the time and date
update_time_date()

# Start the main loop
window.mainloop()

