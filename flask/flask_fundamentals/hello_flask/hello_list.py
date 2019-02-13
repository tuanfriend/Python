from flask import Flask, render_template
app = Flask(__name__)

@app.route("/lists")
def render_lists():
    student_info = [
        {"name": "Michael", "age": 35},
        {"name": "Tom", "age": 29},
        {"name": "Jolie", "age": 31}
    ]

    return render_template("lists.html", random_numbers=[1,2,5], students = student_info)

if __name__ =="__main__":
    app.run(debug=True)