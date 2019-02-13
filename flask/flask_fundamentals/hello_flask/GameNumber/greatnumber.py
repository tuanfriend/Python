from flask import Flask, redirect, render_template, request, session
import random
app = Flask(__name__)
app.secret_key = 'du ma'

@app.route("/")
def index():
    session['number'] = random.randint(1, 100)
    return render_template("numbers.html")

@app.route("/", methods=['POST'])
def guess_game():
    game=""
    print(request.form)
    guessnumber = request.form['guessnumber']
    if int(guessnumber) < session['number']:
        game = "<div class='red'><Strong>Too Low!</Strong></div>"
    elif int(guessnumber) > session['number']:
        game = "<div class='red'><Strong>Too High!</Strong></div>"
    else:
        game = "<div class='green'><Strong>Bingo!!!!!!!</Strong><br><a href='/reset'><button>Play Again</button></a></div>"
    return render_template('numbers.html', game=game)

@app.route("/reset")
def reset():
    session.clear()
    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True)