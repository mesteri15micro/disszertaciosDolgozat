import tkinter as tk
from tkinter import filedialog
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
    "TSP_Visualization"
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
time_var = tk.StringVar()
time_entry = tk.Entry(window, textvariable=time_var)
time_entry.pack()

# Button to start the program
start_button = tk.Button(window, text="Start", command=handle_click)
start_button.pack()

# Button to exit the program
exit_button = tk.Button(window, text="Exit", command=window.destroy)
exit_button.pack()

# Start the main loop
window.mainloop()
