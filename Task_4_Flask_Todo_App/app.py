from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory storage
tasks = []

# Home route
@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

# Add task
@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect("/")

# Delete task
@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)