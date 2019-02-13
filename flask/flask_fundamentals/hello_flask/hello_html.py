from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_html():
    return render_template("index.html", phrase="Hello", times = 5)

@app.route("/<name>/<id>")
def hello_name(name,id):
    print(name)
    return render_template("name.html", some_name=name, num=int(id))

if __name__=="__main__":
    app.run(debug=True)