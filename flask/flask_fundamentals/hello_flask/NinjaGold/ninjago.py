from flask import Flask, redirect, render_template, request, session
import random
app = Flask(__name__)
app.secret_key = 'du ma'

@app.route("/")
def index():
    if 'money' not in session:
        session['activites'] = ""
        session['money'] = 0
    return render_template("ninja.html",money=session['money'], activites=session['activites'])

@app.route("/process_money", methods=['POST'])
def ninja_game():
    temp = session['money']
    if request.form['building'] == 'farm':
        session['money'] += random.randint(10, 20)
        session['activites'] += "Earned "+ str(session['money']-temp) +" from the Farm! \n"
    if request.form['building'] == 'cave':
        session['money'] += random.randint(5, 10)
        session['activites'] += "Earned "+ str(session['money']-temp) +" from the Cave! \n"
    if request.form['building'] == 'house':
        session['money'] += random.randint(2, 5)
        session['activites'] += "Earned "+ str(session['money']-temp) +" from the House! \n"
    if request.form['building'] == 'casino':
        if (random.randint(1, 2)%2) == 0:
            session['money'] += random.randint(0, 50)
            session['activites'] += "You entered casino and win "+ str(session['money']-temp) +" from the Casino! \n"
        else:
            session['money'] -= random.randint(0, 50)
            session['activites'] += "You entered casino and lost "+ str(session['money']-temp) +" from the Casino! \n"
    return redirect('/')

@app.route("/reset")
def reset():
    session.clear()
    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True)