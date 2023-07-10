from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

# Function to handle button click
def handle_click():
    selected_task = request.form.get('task')

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
    elif selected_task == "visualize_cnf_satisfiability":
        subprocess.Popen(["python", "CNF_SatisfiabilityVisualization.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif selected_task == "parhuzamosProgramozasNPTeljesFeladatokra4":
        subprocess.Popen(["python", "parhuzamosProgramozasNPTeljesFeladatokra4.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        handle_click()
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
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)