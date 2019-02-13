from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'du ma'

@app.route("/")
def index():
    if 'count' in session:
        session['count'] += 1
        print('KEY EXISTS!')
    else:
        print('NOT EXIST')
        session['count'] = 0
    return render_template("counter.html", count = session['count'])


@app.route("/reset")
def reset():
    session.clear()
    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True)