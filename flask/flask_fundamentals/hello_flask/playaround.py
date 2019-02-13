from flask import Flask, render_template
app= Flask(__name__)

@app.route("/play")
def playfirst():
    return render_template("level1.html",num=3)

@app.route("/play/<id>")
def leveltwo(id):
    return render_template("level2.html",num=int(id))

@app.route("/play/<id>/<color>")
def levelthree(id,color):
    return render_template("level3.html",num=int(id), box_color=color)

if __name__ =="__main__":
    app.run(debug=True)
