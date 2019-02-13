from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process_form():
    # name_from=""
    # location_from=""
    # language_from=""
    # comment_from=""
    print("Got Post Info")
    print(request.form)
    session['name_from'] = request.form['name']
    session['location_from'] = request.form['location']
    session['language_from'] = request.form['lang']
    session['comment_from'] = request.form['comment']
    return redirect("/result")

@app.route("/result")
def result():
    return render_template("result.html", name_on_temp=session['name_from'], location_on_temp=session['location_from'], lang_on_temp= session['language_from'], comment_on_temp = session['comment_from'])

if __name__ =="__main__":
    app.run(debug=True)