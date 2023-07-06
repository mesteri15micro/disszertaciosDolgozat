import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import time
import sys
import subprocess

# Function to handle button click
def handle_click():
    # Get user selections
    selected_task = task_var.get()
    input_file = file_var.get()
    output_location = output_var.get()
    running_time = time_var.get()

    # Perform actions based on user selections
    if selected_task == "binpackingVisualization":
        subprocess.Popen(["python", "binpackingVisualization.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif selected_task == "Cristofides_Visualization":
        subprocess.Popen(["python", "Cristofides_Visualization.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif selected_task == "graphColoringVisualization":
        subprocess.Popen(["python", "graphColoringVisualization.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif selected_task == "hamiltonCircleVisualization":
        subprocess.Popen(["python", "hamiltonCircleVisualization.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif selected_task == "knapsackVisualization":
        subprocess.Popen(["python", "knapsackVisualization.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif selected_task == "TSP_Visualization":
        subprocess.Popen(["python", "TSP_Visualization.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif selected_task == "dodekaeder":
        subprocess.Popen(["python", "dodekaeder.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif selected_task == "knapsack_brute_force":
        subprocess.Popen(["python", "knapsack_brute_force.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif selected_task == "parhuzamosProgramozasNPTeljesFeladatokra4":
        subprocess.Popen(["python", "kparhuzamosProgramozasNPTeljesFeladatokra4.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)            

# Create the main window
window = tk.Tk()
window.title("Customized User Interface")
window.geometry("400x300")


# Option 1: Choose NP complete task
tasks = [
    "binpackingVisualization",
    "Cristofides_Visualization",
    "graphColoringVisualization",
    "hamiltonCircleVisualization",
    "knapsackVisualization",
    "TSP_Visualization",
    "dodekaeder",
    "knapsack_brute_force",
    "parhuzamosProgramozasNPTeljesFeladatokra4"
]
task_var = tk.StringVar()
task_var.set(tasks[0])
task_dropdown = tk.OptionMenu(window, task_var, *tasks)
task_dropdown.pack()


# Option 2: Select input data files
file_var = tk.StringVar()
file_button = tk.Button(window, text="Browse", command=lambda: file_var.set(filedialog.askopenfilename()))
file_button.pack()

# Option 3: Choose output data location
output_var = tk.StringVar()
output_entry = tk.Entry(window, textvariable=output_var)
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

# Button to exit the program
exit_button = tk.Button(window, text="Exit", command=window.destroy)
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
