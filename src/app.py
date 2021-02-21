from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#New empty list of todo tasks. 
tasks = []

@app.route('/', methods=["GET", "POST"])
def todoApp():
    if request.method == 'POST':
        newTask = request.form["addTask"]
        
        #Add the new task when input field isn't empty and the task
        # is not already in the list of tasks.

        if (len(newTask) > 0) and (newTask not in tasks): 
            tasks.append(newTask)
    
    return render_template('index.html', tasks=tasks)



@app.route("/delete_task/<task>")
def delete_task(task):

    tasks.remove(task)
    return redirect(url_for("todoApp"))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
