# disszertaciosDolgozat 2023
Szoftverfejlesztés

Forrás:
Sara Baase, Computer Algorithms, Introduction to Design and Analysis, San Diego State University, Addison-Wesley Publishing Company, 1st edition, 1978.

OpenAI. Gpt-3.5 (chatgpt) Guide code explanations. 2023. https://chat.openai.com/c/6e7d931e-78a4-4acf-8416-723cffe78800

Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein (fordítók: Iványi Antal, and Benczur András). Új algoritmusok. Scolar Informatika, Budapest, 2nd edition, 2003. 







// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file


Note: As the brute force approach generates all possible subsets, it can be computationally expensive and impractical for large instances of the knapsack problem. Dynamic programming or other optimized algorithms are usually preferred for real-world applications.


#In this program, we use the NetworkX library for graph creation and manipulation. We define a function create_dodecahedron_graph() that creates an empty graph and adds nodes and edges corresponding to the vertices and edges of a dodecahedron.

#The edges are defined using a list of tuples, where each tuple represents an edge between two vertices. We add these edges to the graph using the add_edges_from() method.

#Finally, we use the draw_circular() function from NetworkX to draw the graph in a circular layout and display it using Matplotlib.

#You can run this Python program to visualize the dodecahedron graph on the Hamilton circle.



Containerize the Python program: Create a Dockerfile that describes the environment and dependencies needed for your Python program. This file will be used to build a Docker image, which is a packaged version of your program along with its dependencies.

Here is the python code which should be containerize in a file named: Custom_UIP_ver04.py

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
        subprocess.Popen(["python", "binpackingVisualization.py", input_file], creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif selected_task == "Cristofides_Visualization":
        subprocess.Popen(["python", "Cristofides_Visualization.py", input_file], creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif selected_task == "graphColoringVisualization":
        subprocess.Popen(["python", "graphColoringVisualization.py", input_file], creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif selected_task == "hamiltonCircleVisualization":
        subprocess.Popen(["python", "hamiltonCircleVisualization.py", input_file], creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif selected_task == "knapsackVisualization":
        subprocess.Popen(["python", "knapsackVisualization.py", input_file], creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif selected_task == "TSP_Visualization":
        subprocess.Popen(["python", "TSP_Visualization.py", input_file], creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif selected_task == "dodekaeder":
        subprocess.Popen(["python", "dodekaeder.py", input_file], creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif selected_task == "visualize_cnf_satisfiability":
        subprocess.Popen(["python", "CNF_SatisfiabilityVisualization.py", input_file], creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif selected_task == "parhuzamosProgramozasNPTeljesFeladatokra4":
        subprocess.Popen(["python", "parhuzamosProgramozasNPTeljesFeladatokra4.py", input_file], creationflags=subprocess.CREATE_NEW_CONSOLE)            

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
    "visualize_cnf_satisfiability",
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









Note that this example assumes you have Docker installed and configured on your machine. Adjust the Dockerfile and commands accordingly if you're using a different setup or platform.

Make sure to save the Dockerfile in the same directory as your Python program, and run the Docker build and run commands from that directory as well.


Here's an example of a `docker-compose.yaml` file that you can use to define and run your Docker container:

```yaml
version: '3'
services:
  myapp:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - 8080:8080
```





To use this `docker-compose.yaml` file:

1. Create a new file named `docker-compose.yaml` (or any name you prefer) in the same directory as your `Dockerfile` and `Custom_UIP_ver04.py` file.

2. Copy the above `docker-compose.yaml` code and paste it into the `docker-compose.yaml` file you created.

3. Open a terminal or command prompt and navigate to the directory containing the `docker-compose.yaml`, `Dockerfile`, and `Custom_UIP_ver04.py` files.

4. Run the following command to start the Docker container using Docker Compose:
   ```
   docker-compose up
   ```

   This command will build the Docker image using the `Dockerfile` and start the container based on the configuration defined in the `docker-compose.yaml` file.

5. Access the Python program running inside the Docker container by opening a web browser and navigating to `http://localhost:8080`. The program's GUI should be accessible in the browser.

This `docker-compose.yaml` file defines a single service named `myapp`. It builds the Docker image using the `Dockerfile` and maps port 8080 from the container to port 8080 on your local machine.

Adjust the port mapping in the `docker-compose.yaml` file if you want to use a different port.

Make sure to save the `docker-compose.yaml` file in the same directory as your `Dockerfile` and `Custom_UIP_ver04.py` files, and run the `docker-compose up` command from that directory as well.


Run the Flask application:
   ```
   python app_2_2.py
   ```



Here's an example of how to change the port mapping from 8080 to 2023:

```
docker run -it -p 2023:8080 customized-ui
```

In this command, the format is `-p <local-port>:<container-port>`. The local port, in this case, is 2023, and the container port is 8080. This means that the application running inside the Docker container on port 8080 will be accessible on port 2023 of your local machine.

After running the above command, you can access the application by opening a web browser and navigating to `http://localhost:2023/`.

Make sure to choose a local port number that is not being used by other services on your machine to avoid conflicts.




Please make sure to adjust the filename and binCapacity variables according to your specific input file and bin capacity requirements.

This program uses a greedy approach to assign each element to the smallest bin that can accommodate it. It sorts the elements in non-increasing order, and then iterates over them, assigning each element to the smallest bin that has enough space for it. It outputs the resulting bins and their contents.

Note that this is an approximation algorithm, and its output may not be optimal in all cases. Specifically, if there are several small elements that collectively could fit into a bin, but are instead split across multiple bins, this algorithm may not produce the optimal solution. However, in practice, this algorithm often produces solutions that are close to optimal, and it runs in polynomial time.


The algorithm colors the vertices of a graph in a way that no two adjacent vertices have the same color. The algorithm iterates through the vertices in ascending order, and assigns each vertex the smallest color c that is not used by any of its adjacent vertices. If all the colors are used by adjacent vertices, the algorithm increments c. The algorithm then assigns the vertex the color c. This process continues until all the vertices are colored.

This implementation uses an adjacency list to represent the graph, and iterates through the list to check the colors of adjacent vertices. The implementation uses a simple loop instead of a while loop, by resetting the loop index to -1 after incrementing the color.


Note that this is a simple implementation and may not always provide an optimal solution, but it can give a reasonably good approximation in many cases. Feel free to modify the code as per your specific requirements.
